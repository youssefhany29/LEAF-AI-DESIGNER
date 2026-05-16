from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "designs.db"

IMAGES_DIR = DATA_DIR / "images"

BULK_IMPORT_DIR = DATA_DIR / "bulk_import"
BULK_IMPORT_IMAGES_DIR = BULK_IMPORT_DIR / "images"
BULK_IMPORT_CSV = BULK_IMPORT_DIR / "designs.csv"

EXPORTS_DIR = DATA_DIR / "exports"


def create_required_folders():
    """
    Create all required project folders if they do not exist.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    BULK_IMPORT_DIR.mkdir(parents=True, exist_ok=True)
    BULK_IMPORT_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)