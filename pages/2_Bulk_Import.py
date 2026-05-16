import streamlit as st

from src.database.design_repository import insert_design
from src.services.import_service import bulk_import_from_csv
from src.ui.shared import setup_page, show_app_header


setup_page("Bulk Import", "📦")
show_app_header()


st.header("📦 Bulk Import Designs")

st.write("""
Use this page when you want to import many designs at once.

Put your CSV file here:

`data/bulk_import/designs.csv`

Put your images here:

`data/bulk_import/images/`
""")

st.subheader("Required CSV Format")

st.code(
    """image_name,product_name,category,subcategory,fit,style,primary_color,secondary_color,pattern,graphic_type,logo_position,sleeve_type,neck_type,season,fabric_look,mood,tags,notes
shirt_0001.jpeg,LEAF Shirt Inspiration 001,T-shirt,Oversized T-shirt,Oversized,Minimal Streetwear,Black,White,Plain,Small chest graphic,Left chest,Short sleeve,Crew neck,Summer,Cotton,Clean premium,"eco,urban,modern","simple front design" """,
    language="csv"
)

if st.button("Start Bulk Import"):
    result = bulk_import_from_csv(insert_design)

    if result["success"]:
        st.success(f"{result['message']} Imported {result['imported']} design(s). ✅")

        if result["skipped"]:
            st.warning(f"Skipped {len(result['skipped'])} row(s).")
            for item in result["skipped"]:
                st.write(f"- {item}")
    else:
        st.error(result["message"])