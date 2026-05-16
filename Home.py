import streamlit as st

from src.ui.shared import setup_page, show_app_header


setup_page("LEAF AI Designer", "🌱")
show_app_header()


st.header("Welcome 👋")

st.write("""
LEAF AI Designer is an AI-powered fashion design assistant.

The goal of this project is to build a system that can:

- store clothing inspiration references
- organize designs by metadata
- search and filter design references
- generate new original design briefs
- later generate clothing mockup images
""")

st.subheader("Current Features ✅")

st.write("""
- Add a single clothing reference
- Bulk import many designs from CSV
- View and search the design library
- Generate a design brief manually
- Generate a design brief from library references
""")

st.subheader("Project Workflow")

st.code(
    """
Dataset → Metadata → Search/Retrieval → Design Brief → Image Generation
""",
    language="text"
)

st.info("Use the pages from the sidebar to continue building your LEAF AI Designer project.")