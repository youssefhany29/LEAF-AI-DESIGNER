import streamlit as st

from src.config import create_required_folders
from src.database.design_repository import init_db


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


def show_app_header():
    """
    Shared app header.
    """
    st.title("🌱 LEAF AI Designer")
    st.write("AI-powered clothing inspiration library and fashion design assistant.")