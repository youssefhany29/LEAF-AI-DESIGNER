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


def is_arabic():
    """
    Return True if current language is Arabic.
    """
    return st.session_state.get("language", "en") == "ar"


def apply_language_direction():
    """
    Apply clean Arabic RTL or English LTR layout.
    """
    if is_arabic():
        st.markdown(
            """
            <style>
            .stApp {
                direction: rtl;
            }

            .main .block-container {
                direction: rtl;
                text-align: right;
                max-width: 1150px;
                padding-top: 3rem;
            }

            section[data-testid="stSidebar"] {
                direction: rtl;
                text-align: right;
            }

            section[data-testid="stSidebar"] * {
                text-align: right;
            }

            div[data-testid="stMarkdownContainer"] {
                direction: rtl;
                text-align: right;
            }

            div[data-testid="stMarkdownContainer"] ul {
                direction: rtl;
                text-align: right;
                list-style-position: inside;
            }

            label, p, h1, h2, h3, h4, h5, h6 {
                direction: rtl;
                text-align: right;
            }

            input, textarea {
                direction: rtl !important;
                text-align: right !important;
            }

            div[data-baseweb="select"] {
                direction: rtl;
                text-align: right;
            }

            div[data-baseweb="select"] * {
                text-align: right;
            }

            .stButton > button {
                direction: rtl;
                text-align: center;
            }

            code, pre, .stCode {
                direction: ltr !important;
                text-align: left !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            .stApp {
                direction: ltr;
            }

            .main .block-container {
                direction: ltr;
                text-align: left;
                max-width: 1150px;
                padding-top: 3rem;
            }

            section[data-testid="stSidebar"] {
                direction: ltr;
                text-align: left;
            }

            div[data-testid="stMarkdownContainer"] {
                direction: ltr;
                text-align: left;
            }

            label, p, h1, h2, h3, h4, h5, h6 {
                direction: ltr;
                text-align: left;
            }

            input, textarea {
                direction: ltr !important;
                text-align: left !important;
            }

            code, pre, .stCode {
                direction: ltr !important;
                text-align: left !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )


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
    apply_language_direction()

    st.title(get_text("app_title"))
    st.write(get_text("app_subtitle"))