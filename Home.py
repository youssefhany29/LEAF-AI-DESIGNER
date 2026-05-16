import streamlit as st

from src.ui.shared import setup_page, show_app_header
from src.translations import get_text


setup_page("LEAF AI Designer", "🌱")
show_app_header()


st.header(get_text("home_welcome"))

st.write(get_text("home_description"))

st.subheader(get_text("current_features"))

st.write("""
- Add a single clothing reference
- Bulk import many designs from CSV
- View and search the design library
- Generate a design brief manually
- Generate a design brief from library references
""")

st.subheader(get_text("workflow"))

st.code(
    """
Dataset → Metadata → Search/Retrieval → Design Brief → Image Generation
""",
    language="text"
)