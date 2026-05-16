import streamlit as st

from src.database.design_repository import get_all_designs
from src.services.analytics_service import (
    rows_to_dataframe,
    count_unique_values,
    get_top_values,
    get_top_tags
)
from src.ui.shared import setup_page, show_app_header
from src.translations import get_text


setup_page("Dataset Analytics", "📊")
show_app_header()

t = get_text

st.header(t("analytics_title"))
st.write(t("analytics_description"))

designs = get_all_designs()
dataframe = rows_to_dataframe(designs)

if dataframe.empty:
    st.info(t("analytics_empty"))
else:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(t("total_designs"), len(dataframe))

    with col2:
        st.metric(t("unique_categories"), count_unique_values(dataframe, "category"))

    with col3:
        st.metric(t("unique_colors"), count_unique_values(dataframe, "primary_color"))

    with col4:
        st.metric(t("unique_styles"), count_unique_values(dataframe, "style"))

    st.markdown("---")

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader(t("top_categories"))
        st.dataframe(
            get_top_values(dataframe, "category"),
            width="stretch",
            hide_index=True
        )

        st.subheader(t("top_fits"))
        st.dataframe(
            get_top_values(dataframe, "fit"),
            width="stretch",
            hide_index=True
        )

    with col_b:
        st.subheader(t("top_colors"))
        st.dataframe(
            get_top_values(dataframe, "primary_color"),
            width="stretch",
            hide_index=True
        )

        st.subheader(t("top_seasons"))
        st.dataframe(
            get_top_values(dataframe, "season"),
            width="stretch",
            hide_index=True
        )

    st.markdown("---")

    st.subheader(t("top_tags"))
    st.dataframe(
        get_top_tags(dataframe),
        width="stretch",
        hide_index=True
    )