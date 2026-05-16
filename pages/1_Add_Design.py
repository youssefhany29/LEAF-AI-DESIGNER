import streamlit as st

from src.constants import CATEGORIES, FITS, SEASONS
from src.database.design_repository import insert_design
from src.services.image_service import save_uploaded_image
from src.ui.shared import setup_page, show_app_header


setup_page("Add Design", "➕")
show_app_header()


st.header("➕ Add New Clothing Reference")

with st.form("add_design_form"):
    product_name = st.text_input(
        "Product Name",
        placeholder="Example: LEAF Shirt Inspiration 001"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        category = st.selectbox("Category", CATEGORIES)
        subcategory = st.text_input(
            "Subcategory",
            placeholder="Example: Oversized T-shirt"
        )
        fit = st.selectbox("Fit", FITS)
        style = st.text_input(
            "Style",
            placeholder="Example: Minimal Streetwear"
        )

    with col2:
        primary_color = st.text_input(
            "Primary Color",
            placeholder="Example: Olive Green"
        )
        secondary_color = st.text_input(
            "Secondary Color",
            placeholder="Example: White"
        )
        pattern = st.text_input(
            "Pattern",
            placeholder="Example: Plain / Graphic / Striped"
        )
        graphic_type = st.text_input(
            "Graphic Type",
            placeholder="Example: Small chest graphic"
        )

    with col3:
        logo_position = st.text_input(
            "Logo Position",
            placeholder="Example: Left chest"
        )
        sleeve_type = st.text_input(
            "Sleeve Type",
            placeholder="Example: Short sleeve"
        )
        neck_type = st.text_input(
            "Neck Type",
            placeholder="Example: Crew neck"
        )
        season = st.selectbox("Season", SEASONS)

    col4, col5 = st.columns(2)

    with col4:
        fabric_look = st.text_input(
            "Fabric Look",
            placeholder="Example: Cotton / Fleece / Denim"
        )
        mood = st.text_input(
            "Mood",
            placeholder="Example: Clean premium / Sporty / Urban"
        )

    with col5:
        tags = st.text_input(
            "Tags",
            placeholder="Example: eco, urban, modern"
        )
        uploaded_image = st.file_uploader(
            "Upload Design Image",
            type=["png", "jpg", "jpeg", "webp"]
        )

    notes = st.text_area(
        "Notes",
        placeholder="Write anything important about this design..."
    )

    submitted = st.form_submit_button("Save Design")

    if submitted:
        if not product_name or not primary_color or not style:
            st.error("Please fill Product Name, Primary Color, and Style.")
        else:
            image_path = save_uploaded_image(uploaded_image)

            insert_design(
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
                image_path=image_path
            )

            st.success("Design reference saved successfully ✅")