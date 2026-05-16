from src.database.connection import get_connection


def insert_generated_design(title, prompt, image_path, notes):
    """
    Save a generated design/mockup into the database.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO generated_designs (
            title,
            prompt,
            image_path,
            notes
        )
        VALUES (?, ?, ?, ?)
    """, (
        title,
        prompt,
        image_path,
        notes
    ))

    connection.commit()
    connection.close()


def get_generated_designs():
    """
    Return all generated designs from newest to oldest.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM generated_designs
        ORDER BY created_at DESC
    """)

    designs = cursor.fetchall()

    connection.close()
    return designs


def update_generated_design_prompt(design_id, prompt, notes):
    """
    Update prompt and notes for a generated design draft.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE generated_designs
        SET
            prompt = ?,
            notes = ?
        WHERE id = ?
    """, (
        prompt,
        notes,
        design_id
    ))

    connection.commit()
    connection.close()


def delete_generated_design(design_id):
    """
    Delete a generated design from the database.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM generated_designs
        WHERE id = ?
    """, (design_id,))

    connection.commit()
    connection.close()