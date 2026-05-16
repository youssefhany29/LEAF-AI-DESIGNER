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
    Apply Arabic RTL or English LTR layout.
    Arabic should read right-to-left, while code blocks stay left-to-right.
    """
    if is_arabic():
        st.markdown(
            """
            <style>
            /* Whole app direction */
            .stApp {
                direction: rtl;
            }

            /* Main content */
            .main .block-container {
                direction: rtl;
                text-align: right;
                max-width: 1100px;
                padding-top: 2rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }

            /* Main text */
            .main .block-container h1,
            .main .block-container h2,
            .main .block-container h3,
            .main .block-container h4,
            .main .block-container h5,
            .main .block-container h6,
            .main .block-container p,
            .main .block-container label,
            .main .block-container span,
            .main .block-container div[data-testid="stMarkdownContainer"] {
                direction: rtl;
                text-align: right;
            }

            /* Lists */
            .main .block-container ul,
            .main .block-container ol {
                direction: rtl;
                text-align: right;
                list-style-position: inside;
                padding-right: 1rem;
                padding-left: 0;
            }

            /* Input fields */
            .main .block-container input,
            .main .block-container textarea {
                direction: rtl !important;
                text-align: right !important;
            }

            /* Select boxes */
            .main .block-container div[data-baseweb="select"],
            .main .block-container div[data-baseweb="select"] * {
                direction: rtl !important;
                text-align: right !important;
            }

            /* Radio buttons */
            .main .block-container div[role="radiogroup"] {
                direction: rtl;
                text-align: right;
            }

            .main .block-container div[role="radiogroup"] label {
                direction: rtl;
                text-align: right;
            }

            /* Buttons */
            .stButton > button {
                direction: rtl;
                text-align: center;
            }

            /* Sidebar */
            section[data-testid="stSidebar"] {
                direction: rtl;
                text-align: right;
            }

            section[data-testid="stSidebar"] * {
                direction: rtl;
                text-align: right;
            }

            /* Keep icons/buttons from breaking */
            section[data-testid="stSidebar"] button,
            section[data-testid="stSidebar"] svg {
                direction: ltr;
            }

            /* Code blocks must stay LTR */
            code, pre, .stCode {
                direction: ltr !important;
                text-align: left !important;
                white-space: pre-wrap !important;
                word-break: break-word !important;
            }

            /* Mobile fixes */
            @media (max-width: 768px) {
                .main .block-container {
                    max-width: 100%;
                    padding-left: 1rem;
                    padding-right: 1rem;
                    padding-top: 1rem;
                    overflow-x: hidden;
                }

                .main .block-container h1 {
                    font-size: 2rem !important;
                    line-height: 1.25 !important;
                    overflow-wrap: break-word !important;
                }

                .main .block-container h2 {
                    font-size: 1.5rem !important;
                    line-height: 1.3 !important;
                    overflow-wrap: break-word !important;
                }

                .main .block-container h3 {
                    font-size: 1.25rem !important;
                    line-height: 1.35 !important;
                }

                .main .block-container p,
                .main .block-container li,
                .main .block-container label {
                    font-size: 1rem !important;
                    line-height: 1.7 !important;
                }

                .main .block-container * {
                    max-width: 100%;
                    overflow-wrap: break-word;
                }

                .stTextInput,
                .stTextArea,
                .stSelectbox,
                .stFileUploader,
                .stButton {
                    width: 100% !important;
                }

                /* Prevent sidebar text becoming vertical */
                section[data-testid="stSidebar"] * {
                    white-space: normal !important;
                    word-break: normal !important;
                    overflow-wrap: break-word !important;
                }
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
                max-width: 1100px;
                padding-top: 2rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }

            .main .block-container h1,
            .main .block-container h2,
            .main .block-container h3,
            .main .block-container h4,
            .main .block-container h5,
            .main .block-container h6,
            .main .block-container p,
            .main .block-container label,
            .main .block-container div[data-testid="stMarkdownContainer"] {
                direction: ltr;
                text-align: left;
            }

            .main .block-container input,
            .main .block-container textarea {
                direction: ltr !important;
                text-align: left !important;
            }

            section[data-testid="stSidebar"] {
                direction: ltr;
                text-align: left;
            }

            section[data-testid="stSidebar"] * {
                direction: ltr;
                text-align: left;
            }

            code, pre, .stCode {
                direction: ltr !important;
                text-align: left !important;
            }

            @media (max-width: 768px) {
                .main .block-container {
                    max-width: 100%;
                    padding-left: 1rem;
                    padding-right: 1rem;
                    padding-top: 1rem;
                    overflow-x: hidden;
                }

                .main .block-container h1 {
                    font-size: 2rem !important;
                    line-height: 1.25 !important;
                }

                .main .block-container h2 {
                    font-size: 1.5rem !important;
                    line-height: 1.3 !important;
                }
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