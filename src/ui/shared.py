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
    Keep Streamlit sidebar/navigation stable on mobile.
    """
    if is_arabic():
        direction = "rtl"
        text_align = "right"
    else:
        direction = "ltr"
        text_align = "left"

    st.markdown(
        f"""
        <style>
        /* Main content direction only */
        .main .block-container {{
            direction: {direction};
            text-align: {text_align};
            max-width: 1100px;
            padding-top: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }}

        /* Text elements */
        .main .block-container h1,
        .main .block-container h2,
        .main .block-container h3,
        .main .block-container h4,
        .main .block-container h5,
        .main .block-container h6,
        .main .block-container p,
        .main .block-container label,
        .main .block-container div[data-testid="stMarkdownContainer"] {{
            direction: {direction};
            text-align: {text_align};
        }}

        /* Lists */
        .main .block-container ul,
        .main .block-container ol {{
            direction: {direction};
            text-align: {text_align};
            list-style-position: inside;
        }}

        /* Inputs */
        .main .block-container input,
        .main .block-container textarea {{
            direction: {direction} !important;
            text-align: {text_align} !important;
        }}

        /* Select boxes in main area only */
        .main .block-container div[data-baseweb="select"] {{
            direction: {direction};
            text-align: {text_align};
        }}

        /* Keep code and CSV examples readable */
        code, pre, .stCode {{
            direction: ltr !important;
            text-align: left !important;
            white-space: pre-wrap !important;
            word-break: break-word !important;
        }}

        /* Sidebar: do NOT force full RTL on all internals */
        section[data-testid="stSidebar"] {{
            direction: {direction};
        }}

        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] {{
            text-align: {text_align};
        }}

        /* Mobile fixes */
        @media (max-width: 768px) {{
            .main .block-container {{
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 1rem;
                max-width: 100%;
                overflow-x: hidden;
            }}

            .main .block-container h1 {{
                font-size: 2rem !important;
                line-height: 1.25 !important;
                word-break: normal !important;
                overflow-wrap: break-word !important;
            }}

            .main .block-container h2 {{
                font-size: 1.6rem !important;
                line-height: 1.3 !important;
                word-break: normal !important;
                overflow-wrap: break-word !important;
            }}

            .main .block-container h3 {{
                font-size: 1.25rem !important;
                line-height: 1.35 !important;
            }}

            .main .block-container p,
            .main .block-container li,
            .main .block-container label {{
                font-size: 1rem !important;
                line-height: 1.6 !important;
            }}

            /* Prevent long text from creating horizontal overflow */
            .main .block-container * {{
                max-width: 100%;
                overflow-wrap: break-word;
            }}

            /* Make widgets fit mobile */
            .stTextInput,
            .stTextArea,
            .stSelectbox,
            .stFileUploader,
            .stButton {{
                width: 100% !important;
            }}
        }}
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