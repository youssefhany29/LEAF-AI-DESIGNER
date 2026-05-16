from pathlib import Path

import streamlit as st

from src.database.design_repository import get_all_designs
from src.services.ml_search_service import (
    search_designs_with_tfidf,
    results_to_dataframe
)
from src.translations import get_text
from src.ui.shared import setup_page, show_app_header


setup_page("ML Search", "🧠")
show_app_header()

t = get_text

st.header(t("ml_search_title"))
st.write(t("ml_search_description"))

designs = get_all_designs()

if len(designs) == 0:
    st.info(t("analytics_empty"))
else:
    query = st.text_input(
        t("ml_query"),
        placeholder=t("ml_query_placeholder")
    )

    top_k = st.slider(
        t("top_k_results"),
        min_value=1,
        max_value=20,
        value=5
    )

    if st.button(t("run_ml_search")):
        results = search_designs_with_tfidf(
            query=query,
            designs=designs,
            top_k=top_k
        )

        if len(results) == 0:
            st.warning(t("ml_search_empty"))
        else:
            st.subheader(t("ml_search_results"))

            dataframe = results_to_dataframe(results)
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