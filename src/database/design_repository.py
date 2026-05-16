import sqlite3
from src.config import DB_PATH, create_required_folders


def get_connection():
    """
    Create and return a SQLite database connection.
    """
    create_required_folders()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    return conn


def init_db():
    """
    Create required database tables if they do not exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS designs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            subcategory TEXT,
            fit TEXT,
            style TEXT NOT NULL,
            primary_color TEXT NOT NULL,
            secondary_color TEXT,
            pattern TEXT,
            graphic_type TEXT,
            logo_position TEXT,
            sleeve_type TEXT,
            neck_type TEXT,
            season TEXT,
            fabric_look TEXT,
            mood TEXT,
            tags TEXT,
            notes TEXT,
            image_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS generated_briefs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT NOT NULL,
            brief TEXT NOT NULL,
            language TEXT NOT NULL,
            reference_names TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def insert_design(
    product_name,
    category,
    subcategory,
    fit,
    style,
    primary_color,
    secondary_color,
    pattern,
    graphic_type,
    logo_position,
    sleeve_type,
    neck_type,
    season,
    fabric_look,
    mood,
    tags,
    notes,
    image_path
):
    """
    Insert a new clothing design/reference into the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO designs (
            product_name,
            category,
            subcategory,
            fit,
            style,
            primary_color,
            secondary_color,
            pattern,
            graphic_type,
            logo_position,
            sleeve_type,
            neck_type,
            season,
            fabric_look,
            mood,
            tags,
            notes,
            image_path
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        product_name,
        category,
        subcategory,
        fit,
        style,
        primary_color,
        secondary_color,
        pattern,
        graphic_type,
        logo_position,
        sleeve_type,
        neck_type,
        season,
        fabric_look,
        mood,
        tags,
        notes,
        image_path
    ))

    conn.commit()
    conn.close()


def normalize_search_words(keyword):
    """
    Convert user search text into searchable English keywords.
    Supports simple Arabic-to-English fashion terms.
    """
    arabic_to_english = {
        "اعمل": [],
        "صمم": [],
        "اكتب": [],
        "لي": [],
        "عايز": [],
        "اريد": [],

        "تيشيرت": ["t-shirt", "shirt"],
        "تشيرت": ["t-shirt", "shirt"],
        "قميص": ["shirt"],
        "هودي": ["hoodie"],
        "سويتشيرت": ["sweatshirt"],
        "بنطلون": ["pants"],
        "شورت": ["shorts"],
        "جاكيت": ["jacket"],
        "كاب": ["cap"],

        "اسود": ["black"],
        "أسود": ["black"],
        "ابيض": ["white"],
        "أبيض": ["white"],
        "رمادي": ["gray"],
        "اخضر": ["green"],
        "أخضر": ["green"],
        "زيتي": ["olive"],
        "ازرق": ["blue"],
        "أزرق": ["blue"],
        "احمر": ["red"],
        "أحمر": ["red"],
        "بيج": ["beige"],
        "بني": ["brown"],

        "واسع": ["oversized", "relaxed"],
        "اوفرسايز": ["oversized"],
        "أوفرسايز": ["oversized"],
        "ضيق": ["slim"],
        "عادي": ["regular"],

        "صيفي": ["summer"],
        "صيف": ["summer"],
        "شتوي": ["winter"],
        "شتاء": ["winter"],

        "قطن": ["cotton"],
        "فليس": ["fleece"],
        "جينز": ["denim"],

        "بسيط": ["minimal"],
        "مينيمال": ["minimal"],
        "ستريت": ["streetwear"],
        "رياضي": ["sporty"],
        "حضري": ["urban"],
        "نضيف": ["clean"],
        "فخم": ["premium"],
        "بيئي": ["eco"],

        "شعار": ["logo"],
        "صدر": ["chest"],
        "ظهر": ["back"],
        "رسمة": ["graphic"],
    }

    stop_words = {
        "make", "create", "design", "a", "an", "the", "for", "with",
        "and", "or", "to", "of", "in", "on", "me", "leaf"
    }

    raw_words = keyword.replace(",", " ").split()
    final_words = []

    for raw_word in raw_words:
        word = raw_word.strip().lower()

        if not word or word in stop_words:
            continue

        if raw_word in arabic_to_english:
            final_words.extend(arabic_to_english[raw_word])
        elif word in arabic_to_english:
            final_words.extend(arabic_to_english[word])
        else:
            final_words.append(word)

    unique_words = []

    for word in final_words:
        if word and word not in unique_words:
            unique_words.append(word)

    return unique_words


def calculate_design_score(design, search_words, category="All", fit="All", season="All"):
    """
    Calculate how relevant a design is to the user's search.

    Higher score = better match.
    """
    score = 0

    weighted_columns = {
        "category": 5,
        "subcategory": 4,
        "fit": 5,
        "style": 4,
        "primary_color": 5,
        "secondary_color": 3,
        "pattern": 2,
        "graphic_type": 4,
        "logo_position": 2,
        "sleeve_type": 2,
        "neck_type": 2,
        "season": 2,
        "fabric_look": 2,
        "mood": 3,
        "tags": 4,
        "notes": 1,
        "product_name": 2,
    }

    for word in search_words:
        for column, weight in weighted_columns.items():
            value = design[column]

            if value is not None and word.lower() in str(value).lower():
                score += weight

    if category != "All" and design["category"] == category:
        score += 10

    if fit != "All" and design["fit"] == fit:
        score += 10

    if season != "All" and design["season"] == season:
        score += 5

    return score


def search_designs(keyword="", category="All", fit="All", season="All"):
    """
    Search designs by keyword words, category, fit, and season.
    Supports English and simple Arabic search terms.

    Results are ranked by relevance score.
    """
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT * FROM designs
        WHERE 1 = 1
    """

    params = []

    searchable_columns = [
        "product_name",
        "category",
        "subcategory",
        "fit",
        "style",
        "primary_color",
        "secondary_color",
        "pattern",
        "graphic_type",
        "logo_position",
        "sleeve_type",
        "neck_type",
        "season",
        "fabric_look",
        "mood",
        "tags",
        "notes"
    ]

    search_words = []

    if keyword:
        search_words = normalize_search_words(keyword)

        if search_words:
            word_conditions = []

            for word in search_words:
                column_conditions = []

                for column in searchable_columns:
                    column_conditions.append(f"{column} LIKE ?")
                    params.append(f"%{word}%")

                word_conditions.append("(" + " OR ".join(column_conditions) + ")")

            query += " AND (" + " OR ".join(word_conditions) + ")"

    if category != "All":
        query += " AND category = ?"
        params.append(category)

    if fit != "All":
        query += " AND fit = ?"
        params.append(fit)

    if season != "All":
        query += " AND season = ?"
        params.append(season)

    query += " ORDER BY created_at DESC"

    cursor.execute(query, params)
    designs = cursor.fetchall()

    conn.close()

    if not search_words and category == "All" and fit == "All" and season == "All":
        return designs

    ranked_designs = sorted(
        designs,
        key=lambda design: calculate_design_score(
            design=design,
            search_words=search_words,
            category=category,
            fit=fit,
            season=season
        ),
        reverse=True
    )

    return ranked_designs

def get_design_by_id(design_id):
    """
    Return one design by ID.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM designs
        WHERE id = ?
    """, (design_id,))

    design = cursor.fetchone()

    conn.close()
    return design


def update_design(
    design_id,
    product_name,
    category,
    subcategory,
    fit,
    style,
    primary_color,
    secondary_color,
    pattern,
    graphic_type,
    logo_position,
    sleeve_type,
    neck_type,
    season,
    fabric_look,
    mood,
    tags,
    notes
):
    """
    Update an existing design metadata record.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE designs
        SET
            product_name = ?,
            category = ?,
            subcategory = ?,
            fit = ?,
            style = ?,
            primary_color = ?,
            secondary_color = ?,
            pattern = ?,
            graphic_type = ?,
            logo_position = ?,
            sleeve_type = ?,
            neck_type = ?,
            season = ?,
            fabric_look = ?,
            mood = ?,
            tags = ?,
            notes = ?
        WHERE id = ?
    """, (
        product_name,
        category,
        subcategory,
        fit,
        style,
        primary_color,
        secondary_color,
        pattern,
        graphic_type,
        logo_position,
        sleeve_type,
        neck_type,
        season,
        fabric_look,
        mood,
        tags,
        notes,
        design_id
    ))

    conn.commit()
    conn.close()


def delete_design(design_id):
    """
    Delete a design from the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM designs
        WHERE id = ?
    """, (design_id,))

    conn.commit()
    conn.close()


def insert_generated_brief(prompt, brief, language, reference_names):
    """
    Save a generated design brief into the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO generated_briefs (
            prompt,
            brief,
            language,
            reference_names
        )
        VALUES (?, ?, ?, ?)
    """, (
        prompt,
        brief,
        language,
        reference_names
    ))

    conn.commit()
    conn.close()


def get_generated_briefs():
    """
    Return all saved generated briefs from newest to oldest.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM generated_briefs
        ORDER BY created_at DESC
    """)

    briefs = cursor.fetchall()

    conn.close()
    return briefs


def delete_generated_brief(brief_id):
    """
    Delete a saved generated brief.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM generated_briefs
        WHERE id = ?
    """, (brief_id,))

    conn.commit()
    conn.close()