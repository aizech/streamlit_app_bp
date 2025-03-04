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
# left_callback: content for the left column (e.g. sidebar navigation)
# middle_callback: main page content
# right_callback: content for the right column (e.g. studio or additional info)
def layout_wa(left_callback, middle_callback, right_callback):

    # --- Load and apply CSS ---
    css_content = load_css_content(config.CSS_FILE)
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

    # --- Logo and Header ---
    logo_text_path = config.ASSETS_DIR / "logo_text.png"
    logo_icon_path = config.ASSETS_DIR / "logo.png"
    # Display logo if files exist
    if logo_icon_path.exists() and logo_text_path.exists():
        st.logo(str(logo_text_path), size="medium", icon_image=str(logo_icon_path))
    else:
        st.title(config.APP_NAME)

    #colored_header(label="Multi-Agent Framework", description="This is a description", color_name="violet-50")

    st.html("""
        <style>
            /* change the button color */
            .stButton button {
                background-color: transparent;
                border: none;
                margin: 0;
            }
        </style>
        """)

    # --- Initialize session state for panel toggles ---
    init_session_state("col1_collapsed", False)
    init_session_state("col3_collapsed", False)

    # --- Helper: dynamic width calculation ---
    def get_column_widths(collapsed_width: float = 0.06):
        if st.session_state["col1_collapsed"] and st.session_state["col3_collapsed"]:
            return collapsed_width, 1 - 2 * collapsed_width, collapsed_width
        elif st.session_state["col1_collapsed"]:
            return collapsed_width, (1 - collapsed_width) / 2, (1 - collapsed_width) / 2
        elif st.session_state["col3_collapsed"]:
            return (1 - collapsed_width) / 2, (1 - collapsed_width) / 2, collapsed_width
        else:
            return 0.3, 0.4, 0.3

    col1_width, col2_width, col3_width = get_column_widths()
    col1, col2, col3 = st.columns([col1_width, col2_width, col3_width], border=True)

    # --- Left Column (Sidebar) ---
    with col1:
        if not st.session_state["col1_collapsed"]:
            #left_inner, left_btn = st.columns([0.8, 0.2], vertical_alignment="center", gap="small")
            #with left_inner:
            #    st.markdown('#### :grey[Sources]')
            #with left_btn:
            #    if st.button(":material/left_panel_close:", key="collapse_col1_button", type="secondary"):
            #        st.session_state["col1_collapsed"] = True
            #        st.rerun()
            ## Call page-specific left content
            #left_callback()
            #st.markdown("<div style='text-align: right;'>", unsafe_allow_html=True)
            if st.button(":material/left_panel_close: Sources", key="collapse_col1_button", type="secondary", help="Collapse left panel"):
                st.session_state["col1_collapsed"] = True
                st.rerun()
            left_callback()
            #st.markdown("</div>", unsafe_allow_html=True)
        else:
            if st.button(":material/left_panel_open:", key="expand_col1_button", type="secondary", help="Expand left panel"):
                st.session_state["col1_collapsed"] = False
                st.rerun()

    # --- Middle Column (Main Content) ---
    with col2:
        st.markdown('#### :grey[Chat]')
        middle_callback()

    # --- Right Column (Studio/Extra Content) ---
    with col3:
        if not st.session_state["col3_collapsed"]:
            #right_inner, right_btn, _ = st.columns([0.8, 0.1, 0.1], vertical_alignment="center", gap="small")
            #with right_inner:
            #    st.markdown('#### :grey[Studio]')
            #with right_btn:
            #    if st.button(":material/left_panel_close:", key="collapse_col3_button", type="secondary"):
            #        st.session_state["col3_collapsed"] = True
            #        st.rerun()
            ## Call page-specific right content
            #right_callback()
            if st.button(":material/right_panel_close: Studio", key="collapse_col3_button", type="secondary", help="Collapse right panel"):
                st.session_state["col3_collapsed"] = True
                st.rerun()
            # Call page-specific right content
            right_callback()
        else:
            if st.button(":material/right_panel_open:", key="expand_col3_button", type="secondary", help="Expand right panel"):
                st.session_state["col3_collapsed"] = False
                st.rerun()

    # Footer will be set in pages directly
    #st.markdown("""<div style="font-size: 14px;">AI can provide incorrect information. Please verify the answers. | Made with :material/favorite: by [Watunga](https://www.watunga.com/)</div>""", unsafe_allow_html=True)
