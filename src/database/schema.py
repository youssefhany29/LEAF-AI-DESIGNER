from src.database.connection import get_connection


def init_db():
    """
    Create all required database tables if they do not exist.
    """
    connection = get_connection()
    cursor = connection.cursor()

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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS generated_designs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            prompt TEXT NOT NULL,
            image_path TEXT,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()