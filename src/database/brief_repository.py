from src.database.connection import get_connection


def insert_generated_brief(prompt, brief, language, reference_names):
    """
    Save a generated design brief into the database.
    """
    connection = get_connection()
    cursor = connection.cursor()

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

    connection.commit()
    connection.close()


def get_generated_briefs():
    """
    Return all saved generated briefs from newest to oldest.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM generated_briefs
        ORDER BY created_at DESC
    """)

    briefs = cursor.fetchall()

    connection.close()
    return briefs


def delete_generated_brief(brief_id):
    """
    Delete a saved generated brief.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM generated_briefs
        WHERE id = ?
    """, (brief_id,))

    connection.commit()
    connection.close()