import streamlit as st

from src.ui.shared import setup_page, show_app_header
from src.translations import get_text


setup_page("LEAF AI Designer", "🌱")
show_app_header()

t = get_text

st.header(t("home_welcome"))
st.write(t("home_description"))

st.subheader(t("current_features"))

st.write(f"""
- {t("feature_add_single")}
- {t("feature_bulk_import")}
- {t("feature_library")}
- {t("feature_manual_brief")}
- {t("feature_library_brief")}
""")

st.subheader(t("workflow"))

st.code(
    """
Dataset → Metadata → Search/Retrieval → Design Brief → Image Generation
""",
    language="text"
)