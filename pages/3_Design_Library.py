from pathlib import Path
import streamlit as st

from src.constants import CATEGORIES, FITS, SEASONS
from src.database.design_repository import search_designs
from src.ui.shared import setup_page, show_app_header


setup_page("Design Library", "📚")
show_app_header()


st.header("📚 Design Library")

col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

with col1:
    keyword = st.text_input(
        "Search designs",
        placeholder="Search by style, color, tag, mood, category..."
    )

with col2:
    category_filter = st.selectbox("Category", ["All"] + CATEGORIES)

with col3:
    fit_filter = st.selectbox("Fit", ["All"] + FITS)

with col4:
    season_filter = st.selectbox("Season", ["All"] + SEASONS)

designs = search_designs(
    keyword=keyword,
    category=category_filter,
    fit=fit_filter,
    season=season_filter
)

if len(designs) == 0:
    st.info("No designs found yet.")
else:
    st.write(f"Found **{len(designs)}** design(s).")

    for design in designs:
        with st.container():
            st.markdown("---")

            col_img, col_info = st.columns([1, 2])

            with col_img:
                if design["image_path"] and Path(design["image_path"]).exists():
                    st.image(design["image_path"], use_container_width=True)
                else:
                    st.info("No image uploaded")

            with col_info:
                st.subheader(design["product_name"])

                c1, c2 = st.columns(2)

                with c1:
                    st.write(f"**Category:** {design['category']}")
                    st.write(f"**Subcategory:** {design['subcategory'] or 'Not specified'}")
                    st.write(f"**Fit:** {design['fit'] or 'Not specified'}")
                    st.write(f"**Style:** {design['style']}")
                    st.write(f"**Primary Color:** {design['primary_color']}")
                    st.write(f"**Secondary Color:** {design['secondary_color'] or 'Not specified'}")
                    st.write(f"**Pattern:** {design['pattern'] or 'Not specified'}")
                    st.write(f"**Graphic Type:** {design['graphic_type'] or 'Not specified'}")

                with c2:
                    st.write(f"**Logo Position:** {design['logo_position'] or 'Not specified'}")
                    st.write(f"**Sleeve Type:** {design['sleeve_type'] or 'Not specified'}")
                    st.write(f"**Neck Type:** {design['neck_type'] or 'Not specified'}")
                    st.write(f"**Season:** {design['season'] or 'Not specified'}")
                    st.write(f"**Fabric Look:** {design['fabric_look'] or 'Not specified'}")
                    st.write(f"**Mood:** {design['mood'] or 'Not specified'}")
                    st.write(f"**Tags:** {design['tags'] or 'No tags'}")

                st.write(f"**Notes:** {design['notes'] or 'No notes'}")
                st.caption(f"Created at: {design['created_at']}")