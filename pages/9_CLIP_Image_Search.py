from pathlib import Path

import streamlit as st

from src.database.design_repository import get_all_designs
from src.services.clip_search_service import (
    search_images_with_clip,
    clip_results_to_dataframe,
    clear_clip_cache
)
from src.translations import get_text
from src.ui.shared import setup_page, show_app_header


setup_page("CLIP Image Search", "🖼️")
show_app_header()

t = get_text

st.header(t("clip_search_title"))
st.write(t("clip_search_description"))
st.info(t("clip_search_warning"))
if st.button(t("clear_clip_cache")):
    clear_clip_cache()
    st.success(t("clip_cache_cleared"))
designs = get_all_designs()

if len(designs) == 0:
    st.info(t("analytics_empty"))
else:
    query = st.text_input(
        t("clip_query"),
        placeholder=t("clip_query_placeholder")
    )

    top_k = st.slider(
        t("top_k_results"),
        min_value=1,
        max_value=20,
        value=5
    )

    if st.button(t("run_clip_search")):
        with st.spinner("Searching images with CLIP..."):
            results = search_images_with_clip(
                query=query,
                designs=designs,
                top_k=top_k
            )

        if len(results) == 0:
            st.warning(t("clip_search_empty"))
        else:
            st.subheader(t("clip_search_results"))

            dataframe = clip_results_to_dataframe(results)
            st.dataframe(dataframe, width="stretch", hide_index=True)

            st.markdown("---")

            for result in results:
                design = result["design"]
                score = result["score"]

                with st.container():
                    col_img, col_info = st.columns([1, 2])

                    with col_img:
                        image_path = design["image_path"]

                        if image_path and Path(image_path).exists():
                            st.image(image_path, width="stretch")
                        else:
                            st.info(t("no_image_uploaded"))

                    with col_info:
                        st.subheader(design["product_name"])
                        st.write(f"**{t('similarity_score')}:** {score:.4f}")
                        st.write(f"**{t('category')}:** {design['category']}")
                        st.write(f"**{t('fit')}:** {design['fit'] or t('not_specified')}")
                        st.write(f"**{t('style')}:** {design['style']}")
                        st.write(f"**{t('primary_color')}:** {design['primary_color']}")
                        st.write(f"**{t('tags')}:** {design['tags'] or t('no_tags')}")
                        st.write(f"**{t('notes')}:** {design['notes'] or t('no_notes')}")

                st.markdown("---")