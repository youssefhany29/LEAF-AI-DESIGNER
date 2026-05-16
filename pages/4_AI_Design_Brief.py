import streamlit as st

from src.constants import CATEGORIES, FITS, SEASONS
from src.database.design_repository import search_designs
from src.services.design_brief_service import (
    generate_design_brief,
    generate_design_brief_from_library
)
from src.ui.shared import setup_page, show_app_header


setup_page("AI Design Brief", "🤖")
show_app_header()


st.header("🤖 AI Design Brief Generator")

st.write(
    "This page has two modes: manual design brief and generated brief from your library."
)

mode = st.radio(
    "Choose Mode",
    [
        "Generate From Library",
        "Manual Design Brief"
    ]
)


if mode == "Generate From Library":
    st.subheader("🧠 Generate New Design From Library References")

    user_prompt = st.text_area(
        "Write your design prompt",
        placeholder="Example: Create a black oversized t-shirt for LEAF with eco streetwear style and a small chest logo."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        category_filter = st.selectbox(
            "Search Category",
            ["All"] + CATEGORIES
        )

    with col2:
        fit_filter = st.selectbox(
            "Search Fit",
            ["All"] + FITS
        )

    with col3:
        season_filter = st.selectbox(
            "Search Season",
            ["All"] + SEASONS
        )

    keyword = st.text_input(
        "Optional search keyword",
        placeholder="Example: black, streetwear, eco, hoodie, cotton"
    )

    if st.button("Generate From Library"):
        if not user_prompt:
            st.error("Please write a design prompt first.")
        else:
            search_keyword = keyword.strip()

            if not search_keyword:
                search_keyword = user_prompt.strip()

            matching_designs = search_designs(
                keyword=search_keyword,
                category=category_filter,
                fit=fit_filter,
                season=season_filter
            )

            st.write(f"Found **{len(matching_designs)}** matching reference design(s).")

            if len(matching_designs) > 0:
                with st.expander("Show references used"):
                    for design in matching_designs[:5]:
                        st.write(
                            f"- {design['product_name']} | "
                            f"{design['category']} | "
                            f"{design['fit']} | "
                            f"{design['style']} | "
                            f"{design['primary_color']}"
                        )

            brief = generate_design_brief_from_library(
                user_prompt=user_prompt,
                matching_designs=matching_designs
            )

            st.markdown(brief)


elif mode == "Manual Design Brief":
    st.subheader("✍️ Manual Design Brief")

    col1, col2, col3 = st.columns(3)

    with col1:
        category = st.selectbox("Product Type", CATEGORIES)
        subcategory = st.text_input(
            "Subcategory",
            placeholder="Example: Oversized T-shirt"
        )
        fit = st.selectbox("Fit", FITS)
        style = st.text_input(
            "Style",
            placeholder="Example: Minimal eco streetwear"
        )

    with col2:
        primary_color = st.text_input(
            "Primary Color",
            placeholder="Example: Sand Beige"
        )
        secondary_color = st.text_input(
            "Secondary Color",
            placeholder="Example: Forest Green"
        )
        pattern = st.text_input(
            "Pattern",
            placeholder="Example: Plain / Graphic / Striped"
        )
        graphic_type = st.text_input(
            "Graphic Type",
            placeholder="Example: Nature-inspired back graphic"
        )

    with col3:
        logo_position = st.text_input(
            "Logo Position",
            placeholder="Example: Small logo on left chest"
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
            placeholder="Example: 240 GSM organic cotton"
        )
        mood = st.text_input(
            "Mood",
            placeholder="Example: Clean premium natural"
        )

    with col5:
        tags = st.text_input(
            "Tags",
            placeholder="Example: eco, minimal, urban"
        )

    notes = st.text_area(
        "Extra Notes",
        placeholder="Example: Summer collection, simple front, medium back print"
    )

    if st.button("Generate Manual Design Brief"):
        if not primary_color or not style:
            st.error("Please enter at least Primary Color and Style.")
        else:
            brief = generate_design_brief(
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

            st.markdown(brief)