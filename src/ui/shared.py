import streamlit as st

from src.config import create_required_folders
from src.database.schema import init_db
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
    Only change text direction/alignment.
    Do not move sidebar or page layout.
    """
    if is_arabic():
        st.markdown(
            """
            <style>
            h1, h2, h3, h4, h5, h6,
            p, label, span,
            div[data-testid="stMarkdownContainer"] {
                direction: rtl !important;
                text-align: right !important;
            }

            input, textarea {
                direction: rtl !important;
                text-align: right !important;
            }

            div[data-baseweb="select"] {
                direction: rtl !important;
                text-align: right !important;
            }

            div[data-baseweb="select"] * {
                text-align: right !important;
            }

            ul, ol {
                direction: rtl !important;
                text-align: right !important;
                list-style-position: inside !important;
            }

            code, pre, .stCode,
            div[data-testid="stCodeBlock"] {
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
            h1, h2, h3, h4, h5, h6,
            p, label, span,
            div[data-testid="stMarkdownContainer"] {
                direction: ltr !important;
                text-align: left !important;
            }

            input, textarea {
                direction: ltr !important;
                text-align: left !important;
            }

            code, pre, .stCode,
            div[data-testid="stCodeBlock"] {
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