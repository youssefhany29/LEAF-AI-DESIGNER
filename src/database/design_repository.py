from src.database.connection import get_connection
from src.services.search_service import (
    build_keyword_conditions,
    calculate_design_score,
    normalize_search_words,
)


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
    connection = get_connection()
    cursor = connection.cursor()

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

    connection.commit()
    connection.close()


def search_designs(keyword="", category="All", fit="All", season="All"):
    """
    Search designs by keyword words, category, fit, and season.
    Results are ranked by relevance score.
    """
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT * FROM designs
        WHERE 1 = 1
    """

    params = []
    search_words = []

    if keyword:
        search_words = normalize_search_words(keyword)
        keyword_condition, keyword_params = build_keyword_conditions(search_words)
        query += keyword_condition
        params.extend(keyword_params)

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

    connection.close()

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
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM designs
        WHERE id = ?
    """, (design_id,))

    design = cursor.fetchone()

    connection.close()
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
    connection = get_connection()
    cursor = connection.cursor()

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

    connection.commit()
    connection.close()


def delete_design(design_id):
    """
    Delete a design from the database.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM designs
        WHERE id = ?
    """, (design_id,))

    connection.commit()
    connection.close()