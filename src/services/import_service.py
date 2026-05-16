from datetime import datetime
import csv
import shutil

from src.config import (
    BULK_IMPORT_CSV,
    BULK_IMPORT_IMAGES_DIR,
    IMAGES_DIR,
    create_required_folders
)


REQUIRED_COLUMNS = [
    "image_name",
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


def bulk_import_from_csv(insert_design_function):
    """
    Import many clothing design references from data/bulk_import/designs.csv.
    """
    create_required_folders()

    if not BULK_IMPORT_CSV.exists():
        return {
            "success": False,
            "message": "designs.csv was not found inside data/bulk_import/",
            "imported": 0,
            "skipped": []
        }

    imported_count = 0
    skipped = []

    with open(BULK_IMPORT_CSV, mode="r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            return {
                "success": False,
                "message": "CSV file is empty or invalid.",
                "imported": 0,
                "skipped": []
            }

        missing_columns = [
            column for column in REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]

        if missing_columns:
            return {
                "success": False,
                "message": f"Missing columns in CSV: {', '.join(missing_columns)}",
                "imported": 0,
                "skipped": []
            }

        for row_number, row in enumerate(reader, start=2):
            image_name = row["image_name"].strip()
            product_name = row["product_name"].strip()
            category = row["category"].strip()
            subcategory = row["subcategory"].strip()
            fit = row["fit"].strip()
            style = row["style"].strip()
            primary_color = row["primary_color"].strip()
            secondary_color = row["secondary_color"].strip()
            pattern = row["pattern"].strip()
            graphic_type = row["graphic_type"].strip()
            logo_position = row["logo_position"].strip()
            sleeve_type = row["sleeve_type"].strip()
            neck_type = row["neck_type"].strip()
            season = row["season"].strip()
            fabric_look = row["fabric_look"].strip()
            mood = row["mood"].strip()
            tags = row["tags"].strip()
            notes = row["notes"].strip()

            if not image_name or not product_name or not category or not style or not primary_color:
                skipped.append(f"Row {row_number}: Missing required data")
                continue

            source_image_path = BULK_IMPORT_IMAGES_DIR / image_name

            if not source_image_path.exists():
                skipped.append(f"Row {row_number}: Image not found: {image_name}")
                continue

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            destination_image_name = f"bulk_{timestamp}_{image_name}"
            destination_image_path = IMAGES_DIR / destination_image_name

            shutil.copy2(source_image_path, destination_image_path)

            insert_design_function(
                product_name=product_name,
                category=category,
                subcategory=subcategory,
                fit=fit,
                style=style,
                primary_color=primary_color,
                secondary_color=secondary_color,
                pattern=pattern,
                graphic_type=graphic_type,
                logo_position=logo_position,
                sleeve_type=sleeve_type,
                neck_type=neck_type,
                season=season,
                fabric_look=fabric_look,
                mood=mood,
                tags=tags,
                notes=notes,
                image_path=str(destination_image_path)
            )

            imported_count += 1

    return {
        "success": True,
        "message": "Bulk import completed.",
        "imported": imported_count,
        "skipped": skipped
    }