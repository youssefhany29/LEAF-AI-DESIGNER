import streamlit as st

from src.constants import CATEGORIES, FITS, SEASONS
from src.database.design_repository import insert_design
from src.services.image_service import save_uploaded_image
from src.ui.shared import setup_page, show_app_header
from src.translations import get_text


setup_page("Add Design", "➕")
show_app_header()

t = get_text

st.header(t("add_design_title"))

with st.form("add_design_form"):
    product_name = st.text_input(
        t("product_name"),
        placeholder=t("ph_product_name")
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        category = st.selectbox(t("category"), CATEGORIES)
        subcategory = st.text_input(
            t("subcategory"),
            placeholder=t("ph_subcategory")
        )
        fit = st.selectbox(t("fit"), FITS)
        style = st.text_input(
            t("style"),
            placeholder=t("ph_style")
        )

    with col2:
        primary_color = st.text_input(
            t("primary_color"),
            placeholder=t("ph_primary_color")
        )
        secondary_color = st.text_input(
            t("secondary_color"),
            placeholder=t("ph_secondary_color")
        )
        pattern = st.text_input(
            t("pattern"),
            placeholder=t("ph_pattern")
        )
        graphic_type = st.text_input(
            t("graphic_type"),
            placeholder=t("ph_graphic_type")
        )

    with col3:
        logo_position = st.text_input(
            t("logo_position"),
            placeholder=t("ph_logo_position")
        )
        sleeve_type = st.text_input(
            t("sleeve_type"),
            placeholder=t("ph_sleeve_type")
        )
        neck_type = st.text_input(
            t("neck_type"),
            placeholder=t("ph_neck_type")
        )
        season = st.selectbox(t("season"), SEASONS)

    col4, col5 = st.columns(2)

    with col4:
        fabric_look = st.text_input(
            t("fabric_look"),
            placeholder=t("ph_fabric")
        )
        mood = st.text_input(
            t("mood"),
            placeholder=t("ph_mood")
        )

    with col5:
        tags = st.text_input(
            t("tags"),
            placeholder=t("ph_tags")
        )
        uploaded_image = st.file_uploader(
            t("upload_design_image"),
            type=["png", "jpg", "jpeg", "webp"]
        )

    notes = st.text_area(
        t("notes"),
        placeholder=t("ph_notes")
    )

    submitted = st.form_submit_button(t("save_design"))

    if submitted:
        if not product_name or not primary_color or not style:
            st.error(t("required_fields_error"))
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

            st.success(t("design_saved_success"))