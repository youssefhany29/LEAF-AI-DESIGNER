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


def apply_language_direction():
    """
    Apply left-to-right or right-to-left layout based on selected language.
    """
    language = st.session_state.get("language", "en")

    if language == "ar":
        st.markdown(
            """
            <style>
            html, body, [class*="css"] {
                direction: rtl;
                text-align: right;
            }

            .stApp {
                direction: rtl;
                text-align: right;
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

            div[data-testid="stTextInput"] label,
            div[data-testid="stTextArea"] label,
            div[data-testid="stSelectbox"] label,
            div[data-testid="stFileUploader"] label {
                direction: rtl;
                text-align: right;
            }

            input, textarea {
                direction: rtl;
                text-align: right;
            }

            .stButton > button {
                direction: rtl;
            }

            code, pre {
                direction: ltr;
                text-align: left;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            html, body, [class*="css"] {
                direction: ltr;
                text-align: left;
            }

            .stApp {
                direction: ltr;
                text-align: left;
            }

            section[data-testid="stSidebar"] {
                direction: ltr;
                text-align: left;
            }

            div[data-testid="stMarkdownContainer"] {
                direction: ltr;
                text-align: left;
            }

            input, textarea {
                direction: ltr;
                text-align: left;
            }

            code, pre {
                direction: ltr;
                text-align: left;
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