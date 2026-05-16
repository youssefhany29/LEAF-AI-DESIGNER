from pathlib import Path

import streamlit as st

from src.constants import CATEGORIES, FITS, SEASONS
from src.services.reference_search_service import (
    SEARCH_METHOD_CLIP,
    SEARCH_METHOD_KEYWORD,
    SEARCH_METHOD_ML,
    extract_designs_from_results,
    find_reference_results,
    get_reference_names
)
from src.database.brief_repository import insert_generated_brief
from src.services.design_brief_service import (
    generate_design_brief,
    generate_design_brief_from_library
)
from src.services.ml_search_service import search_designs_with_tfidf
from src.ui.shared import setup_page, show_app_header
from src.translations import get_text


setup_page("AI Design Brief", "🤖")
show_app_header()

t = get_text

st.header(t("ai_brief_title"))
st.write(t("ai_brief_description"))

mode = st.radio(
    t("choose_mode"),
    [
        t("generate_from_library"),
        t("manual_design_brief")
    ]
)


def get_current_language():
    """
    Return current selected language.
    """
    return st.session_state.get("language", "en")

def show_reference_board(reference_results):
    """
    Show the reference images used to generate the design brief.
    Includes similarity scores when available.
    """
    if len(reference_results) == 0:
        return

    st.subheader(t("reference_board_title"))

    max_references_to_show = min(len(reference_results), 6)
    references = reference_results[:max_references_to_show]
    columns_per_row = 3

    for start_index in range(0, len(references), columns_per_row):
        row_items = references[start_index:start_index + columns_per_row]
        columns = st.columns(columns_per_row)

        for column, result in zip(columns, row_items):
            design = result["design"]
            score = result["score"]

            with column:
                image_path = design["image_path"]

                if image_path and Path(image_path).exists():
                    st.image(image_path, width="stretch")
                else:
                    st.info(t("no_image_uploaded"))

                st.markdown(f"**{design['product_name']}**")
                st.caption(
                    f"{design['category']} | "
                    f"{design['fit']} | "
                    f"{design['style']} | "
                    f"{design['primary_color']}"
                )

                if score is not None:
                    st.write(f"**{t('similarity_score')}:** {score:.4f}")

def save_last_brief_button():
    """
    Show save button for the last generated brief.
    """
    if "last_generated_brief" not in st.session_state:
        return

    if st.button(t("save_generated_brief")):
        insert_generated_brief(
            prompt=st.session_state["last_generated_prompt"],
            brief=st.session_state["last_generated_brief"],
            language=st.session_state["last_generated_language"],
            reference_names=st.session_state["last_reference_names"]
        )

        st.success(t("brief_saved_success"))


if mode == t("generate_from_library"):
    st.subheader(t("generate_from_library_title"))

    user_prompt = st.text_area(
        t("write_prompt"),
        placeholder=t("prompt_placeholder")
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        category_options = ["All"] + CATEGORIES
        category_display = [t("all")] + CATEGORIES
        selected_category_display = st.selectbox(t("search_category"), category_display)
        category_filter = category_options[category_display.index(selected_category_display)]

    with col2:
        fit_options = ["All"] + FITS
        fit_display = [t("all")] + FITS
        selected_fit_display = st.selectbox(t("search_fit"), fit_display)
        fit_filter = fit_options[fit_display.index(selected_fit_display)]

    with col3:
        season_options = ["All"] + SEASONS
        season_display = [t("all")] + SEASONS
        selected_season_display = st.selectbox(t("search_season"), season_display)
        season_filter = season_options[season_display.index(selected_season_display)]

    keyword = st.text_input(
        t("optional_keyword"),
        placeholder=t("keyword_placeholder")
    )

    search_method_labels = {
        t("keyword_search"): SEARCH_METHOD_KEYWORD,
        t("ml_search"): SEARCH_METHOD_ML,
        t("clip_image_search"): SEARCH_METHOD_CLIP,
    }

    selected_search_method_label = st.radio(
        t("search_method"),
        list(search_method_labels.keys()),
        horizontal=True
    )

    search_method = search_method_labels[selected_search_method_label]

    if search_method == SEARCH_METHOD_ML:
        st.info(t("ml_search_note"))

    if search_method == SEARCH_METHOD_CLIP:
        st.info(t("clip_search_note"))

    if search_method == t("ml_search"):
        st.info(t("ml_search_note"))

    if st.button(t("generate_button")):
        if not user_prompt:
            st.error(t("write_prompt_error"))
        else:
            reference_results = find_reference_results(
                user_prompt=user_prompt,
                keyword=keyword,
                category_filter=category_filter,
                fit_filter=fit_filter,
                season_filter=season_filter,
                search_method=search_method,
                top_k=10
            )

            matching_designs = extract_designs_from_results(reference_results)
            reference_names_text = get_reference_names(matching_designs)

            brief = generate_design_brief_from_library(
                user_prompt=user_prompt,
                matching_designs=matching_designs
            )

            st.session_state["last_reference_results"] = reference_results
            st.session_state["last_matching_designs"] = matching_designs
            st.session_state["last_generated_prompt"] = user_prompt
            st.session_state["last_generated_brief"] = brief
            st.session_state["last_generated_language"] = get_current_language()
            st.session_state["last_reference_names"] = reference_names_text

    if "last_generated_brief" in st.session_state:
        matching_designs = st.session_state.get("last_matching_designs", [])
        reference_results = st.session_state.get("last_reference_results", [])

        st.write(f"{t('found_designs')} **{len(matching_designs)}** {t('matching_refs_found')}")

        if len(reference_results) > 0:
            show_reference_board(reference_results)

            with st.expander(t("show_references")):
                for design in matching_designs[:5]:
                    st.write(
                        f"- {design['product_name']} | "
                        f"{design['category']} | "
                        f"{design['fit']} | "
                        f"{design['style']} | "
                        f"{design['primary_color']}"
                    )

        st.markdown(st.session_state["last_generated_brief"])
        save_last_brief_button()


elif mode == t("manual_design_brief"):
    st.subheader(t("manual_brief_title"))

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

    notes = st.text_area(
        t("notes"),
        placeholder=t("ph_notes")
    )

    if st.button(t("generate_manual_button")):
        if not primary_color or not style:
            st.error(t("required_fields_error"))
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

            st.session_state["last_generated_prompt"] = notes if notes else "Manual design brief"
            st.session_state["last_generated_brief"] = brief
            st.session_state["last_generated_language"] = get_current_language()
            st.session_state["last_reference_names"] = "Manual brief"

    if "last_generated_brief" in st.session_state:
        st.markdown(st.session_state["last_generated_brief"])
        save_last_brief_button()