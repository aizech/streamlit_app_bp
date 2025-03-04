# layout_wa.py
import streamlit as st
import sys
from pathlib import Path

# Add the parent directory to sys.path
file_path = Path(__file__).parent.parent
sys.path.insert(0, str(file_path))

from config_wa import config

# Helper: load CSS content and cache it.
@st.cache_data(show_spinner=False)
def load_css_content(file_path: Path) -> str:
    with file_path.open() as f:
        return f.read()

# Helper: initialize a session state key if not already set.
def init_session_state(key: str, default):
    st.session_state.setdefault(key, default)

# Common layout function that accepts three callbacks:
# main_callback: main content
# left_callback: content for the left column (e.g. sidebar navigation)
# middle_callback: content for the middle column (e.g. main page content)
# right_callback: content for the right column (e.g. studio or additional info)
def layout_simple_wa(main_callback, left_callback=None, middle_callback=None, right_callback=None):

    # --- Load and apply CSS ---
    css_content = load_css_content(config.CSS_FILE)
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

    # --- Logo and Header ---
    logo_text_path = config.ASSETS_DIR / "logo_text.png"
    logo_icon_path = config.ASSETS_DIR / "logo.png"
    # Display logo if files exist
    if logo_icon_path.exists() and logo_text_path.exists():
        st.logo(str(logo_text_path), size="small", icon_image=str(logo_icon_path))
    else:
        st.title(config.APP_NAME)

    #colored_header(label="Multi-Agent Framework", description="This is a description", color_name="violet-50")

    st.html("""
        <style>
            /* change the button color */
            #.stButton button {
            #    background-color: transparent;
            #    border: none;
            #    margin: 0;
            #}
        </style>
        """)

    # --- Initialize session state for panel toggles ---
    init_session_state("col1_collapsed", False)
    init_session_state("col3_collapsed", False)

    # --- Layout ---

    # --- Main Container (Main Content) ---
    if main_callback is not None:
        main = st.container()
        with main:
            #st.markdown(':material/chat: :grey[Chat]')
            main_callback()
    else:
        pass

    # --- Dynamic Column Layout based on provided callbacks ---
    columns_config = []
    callbacks = []
    if left_callback is not None:
        columns_config.append(1)
        callbacks.append(left_callback)
    if middle_callback is not None:
        columns_config.append(3)
        callbacks.append(middle_callback)
    if right_callback is not None:
        columns_config.append(1)
        callbacks.append(right_callback)

    if not columns_config:
        st.empty()
        return
    cols = st.columns(columns_config)
    for idx, cb in enumerate(callbacks):
        with cols[idx]:
            cb()

    # Footer will be set in pages directly
    #st.markdown("""<div style="font-size: 14px;">AI can provide incorrect information. Please verify the answers. | Made with :material/favorite: by [Watunga](https://www.watunga.com/)</div>""", unsafe_allow_html=True)
