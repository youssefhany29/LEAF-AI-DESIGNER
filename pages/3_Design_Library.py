from pathlib import Path
import streamlit as st

from src.constants import CATEGORIES, FITS, SEASONS
from src.database.design_repository import search_designs
from src.ui.shared import setup_page, show_app_header
from src.translations import get_text


setup_page("Design Library", "📚")
show_app_header()

t = get_text

st.header(t("design_library_title"))

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