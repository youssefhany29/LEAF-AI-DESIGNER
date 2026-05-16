import sqlite3

from src.config import DB_PATH, create_required_folders


def get_connection():
    """
    Create and return a SQLite database connection.
    """
    create_required_folders()

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    return connection