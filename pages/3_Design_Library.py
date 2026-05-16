from pathlib import Path
import os

import streamlit as st

from src.constants import CATEGORIES, FITS, SEASONS
from src.database.design_repository import (
    search_designs,
    update_design,
    delete_design
)
from src.ui.shared import setup_page, show_app_header
from src.translations import get_text


setup_page("Design Library", "📚")
show_app_header()

t = get_text

st.header(t("design_library_title"))


def get_index(options, value):
    """
    Return index of value in options.
    If value does not exist, return 0.
    """
    if value in options:
        return options.index(value)

    return 0


def show_design_details(design):
    """
    Display design metadata.
    """
    c1, c2 = st.columns(2)

    with c1:
        st.write(f"**{t('category')}:** {design['category']}")
        st.write(f"**{t('subcategory')}:** {design['subcategory'] or t('not_specified')}")
        st.write(f"**{t('fit')}:** {design['fit'] or t('not_specified')}")
        st.write(f"**{t('style')}:** {design['style']}")
        st.write(f"**{t('primary_color')}:** {design['primary_color']}")
        st.write(f"**{t('secondary_color')}:** {design['secondary_color'] or t('not_specified')}")
        st.write(f"**{t('pattern')}:** {design['pattern'] or t('not_specified')}")
        st.write(f"**{t('graphic_type')}:** {design['graphic_type'] or t('not_specified')}")

    with c2:
        st.write(f"**{t('logo_position')}:** {design['logo_position'] or t('not_specified')}")
        st.write(f"**{t('sleeve_type')}:** {design['sleeve_type'] or t('not_specified')}")
        st.write(f"**{t('neck_type')}:** {design['neck_type'] or t('not_specified')}")
        st.write(f"**{t('season')}:** {design['season'] or t('not_specified')}")
        st.write(f"**{t('fabric_look')}:** {design['fabric_look'] or t('not_specified')}")
        st.write(f"**{t('mood')}:** {design['mood'] or t('not_specified')}")
        st.write(f"**{t('tags')}:** {design['tags'] or t('no_tags')}")

    st.write(f"**{t('notes')}:** {design['notes'] or t('no_notes')}")
    st.caption(f"{t('created_at')}: {design['created_at']}")


def show_edit_form(design):
    """
    Display edit form for one design.
    """
    with st.form(f"edit_design_form_{design['id']}"):
        st.subheader(t("edit_design"))

        product_name = st.text_input(
            t("product_name"),
            value=design["product_name"]
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            category = st.selectbox(
                t("category"),
                CATEGORIES,
                index=get_index(CATEGORIES, design["category"])
            )

            subcategory = st.text_input(
                t("subcategory"),
                value=design["subcategory"] or ""
            )

            fit = st.selectbox(
                t("fit"),
                FITS,
                index=get_index(FITS, design["fit"])
            )

            style = st.text_input(
                t("style"),
                value=design["style"] or ""
            )

        with col2:
            primary_color = st.text_input(
                t("primary_color"),
                value=design["primary_color"] or ""
            )

            secondary_color = st.text_input(
                t("secondary_color"),
                value=design["secondary_color"] or ""
            )

            pattern = st.text_input(
                t("pattern"),
                value=design["pattern"] or ""
            )

            graphic_type = st.text_input(
                t("graphic_type"),
                value=design["graphic_type"] or ""
            )

        with col3:
            logo_position = st.text_input(
                t("logo_position"),
                value=design["logo_position"] or ""
            )

            sleeve_type = st.text_input(
                t("sleeve_type"),
                value=design["sleeve_type"] or ""
            )

            neck_type = st.text_input(
                t("neck_type"),
                value=design["neck_type"] or ""
            )

            season = st.selectbox(
                t("season"),
                SEASONS,
                index=get_index(SEASONS, design["season"])
            )

        col4, col5 = st.columns(2)

        with col4:
            fabric_look = st.text_input(
                t("fabric_look"),
                value=design["fabric_look"] or ""
            )

            mood = st.text_input(
                t("mood"),
                value=design["mood"] or ""
            )

        with col5:
            tags = st.text_input(
                t("tags"),
                value=design["tags"] or ""
            )

            notes = st.text_area(
                t("notes"),
                value=design["notes"] or ""
            )

        submitted = st.form_submit_button(t("save_changes"))

        if submitted:
            if not product_name or not primary_color or not style:
                st.error(t("required_fields_error"))
            else:
                update_design(
                    design_id=design["id"],
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
                    notes=notes
                )

                st.success(t("design_updated_success"))
                st.rerun()


def delete_design_ui(design):
    """
    Display delete section for one design.
    """
    st.warning(t("delete_warning"))

    delete_image_too = st.checkbox(
        t("delete_image_too"),
        key=f"delete_image_{design['id']}"
    )

    confirm_delete = st.text_input(
        t("type_delete_to_confirm"),
        key=f"confirm_delete_{design['id']}"
    )

    if st.button(t("delete_design"), key=f"delete_btn_{design['id']}"):
        if confirm_delete.strip().upper() != "DELETE":
            st.error(t("delete_confirm_error"))
            return

        image_path = design["image_path"]

        delete_design(design["id"])

        if delete_image_too and image_path and Path(image_path).exists():
            try:
                os.remove(image_path)
            except OSError:
                st.warning(t("image_delete_warning"))

        st.success(t("design_deleted_success"))
        st.rerun()


col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

with col1:
    keyword = st.text_input(
        t("search_designs"),
        placeholder=t("search_placeholder")
    )

with col2:
    category_options = ["All"] + CATEGORIES
    category_display = [t("all")] + CATEGORIES
    selected_category_display = st.selectbox(t("category"), category_display)
    category_filter = category_options[category_display.index(selected_category_display)]

with col3:
    fit_options = ["All"] + FITS
    fit_display = [t("all")] + FITS
    selected_fit_display = st.selectbox(t("fit"), fit_display)
    fit_filter = fit_options[fit_display.index(selected_fit_display)]

with col4:
    season_options = ["All"] + SEASONS
    season_display = [t("all")] + SEASONS
    selected_season_display = st.selectbox(t("season"), season_display)
    season_filter = season_options[season_display.index(selected_season_display)]

designs = search_designs(
    keyword=keyword,
    category=category_filter,
    fit=fit_filter,
    season=season_filter
)

if len(designs) == 0:
    st.info(t("no_designs_found"))
else:
    st.write(f"{t('found_designs')} **{len(designs)}** {t('designs')}.")

    for design in designs:
        with st.container():
            st.markdown("---")

            col_img, col_info = st.columns([1, 2])

            with col_img:
                if design["image_path"] and Path(design["image_path"]).exists():
                    st.image(design["image_path"], width="stretch")
                else:
                    st.info(t("no_image_uploaded"))

            with col_info:
                st.subheader(design["product_name"])

                show_design_details(design)

                manage_mode = st.radio(
                    t("manage_design"),
                    [
                        t("view_only"),
                        t("edit_design"),
                        t("delete_design")
                    ],
                    horizontal=True,
                    key=f"manage_mode_{design['id']}"
                )

                if manage_mode == t("edit_design"):
                    show_edit_form(design)

                elif manage_mode == t("delete_design"):
                    delete_design_ui(design)