import streamlit as st

from src.config import create_required_folders
from src.database.design_repository import init_db
from src.translations import get_text


def setup_page(title, icon="🌱"):
    """
    Shared setup for all Streamlit pages.
    """
    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout="wide"
    )

    create_required_folders()
    init_db()

    if "language" not in st.session_state:
        st.session_state.language = "en"


def language_selector():
    """
    Sidebar language selector.
    """
    language_options = {
        "English": "en",
        "العربية": "ar"
    }

    current_language = st.session_state.get("language", "en")

    selected_label = st.sidebar.selectbox(
        get_text("language"),
        options=list(language_options.keys()),
        index=list(language_options.values()).index(current_language)
    )

    st.session_state.language = language_options[selected_label]


def show_app_header():
    """
    Shared app header.
    """
    language_selector()

    st.title(get_text("app_title"))
    st.write(get_text("app_subtitle"))