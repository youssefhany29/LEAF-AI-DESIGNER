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
    Create the designs table if it does not exist.
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


def search_designs(keyword="", category="All", fit="All", season="All"):
    """
    Search designs by keyword words, category, fit, and season.

    Example:
    'make black oversized shirt'
    becomes:
    search for black OR oversized OR shirt
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

    stop_words = {
        "make", "create", "design", "a", "an", "the", "for", "with",
        "and", "or", "to", "of", "in", "on", "me", "leaf"
    }

    if keyword:
        words = [
            word.strip().lower()
            for word in keyword.replace(",", " ").split()
            if word.strip().lower() not in stop_words
        ]

        if words:
            word_conditions = []

            for word in words:
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
    return designs