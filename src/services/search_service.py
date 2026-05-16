SEARCHABLE_COLUMNS = [
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
    "notes",
]


WEIGHTED_COLUMNS = {
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


ARABIC_TO_ENGLISH = {
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


STOP_WORDS = {
    "make", "create", "design", "a", "an", "the", "for", "with",
    "and", "or", "to", "of", "in", "on", "me", "leaf"
}


def normalize_search_words(keyword):
    """
    Convert user search text into searchable English keywords.
    Supports simple Arabic-to-English fashion terms.
    """
    raw_words = keyword.replace(",", " ").split()
    final_words = []

    for raw_word in raw_words:
        word = raw_word.strip().lower()

        if not word or word in STOP_WORDS:
            continue

        if raw_word in ARABIC_TO_ENGLISH:
            final_words.extend(ARABIC_TO_ENGLISH[raw_word])
        elif word in ARABIC_TO_ENGLISH:
            final_words.extend(ARABIC_TO_ENGLISH[word])
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
    """
    score = 0

    for word in search_words:
        for column, weight in WEIGHTED_COLUMNS.items():
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


def build_keyword_conditions(search_words):
    """
    Build SQL LIKE conditions and params for search words.
    """
    if not search_words:
        return "", []

    params = []
    word_conditions = []

    for word in search_words:
        column_conditions = []

        for column in SEARCHABLE_COLUMNS:
            column_conditions.append(f"{column} LIKE ?")
            params.append(f"%{word}%")

        word_conditions.append("(" + " OR ".join(column_conditions) + ")")

    condition_sql = " AND (" + " OR ".join(word_conditions) + ")"

    return condition_sql, params