from pathlib import Path
from datetime import datetime
from PIL import Image

from src.config import IMAGES_DIR, create_required_folders


def save_uploaded_image(uploaded_file):
    """
    Save uploaded image inside data/images and return its path as text.
    """
    if uploaded_file is None:
        return None

    create_required_folders()

    file_extension = Path(uploaded_file.name).suffix
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    file_name = f"design_{timestamp}{file_extension}"
    image_path = IMAGES_DIR / file_name

    image = Image.open(uploaded_file)
    image.save(image_path)

    return str(image_path)