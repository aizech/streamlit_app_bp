# Page: Template_Page_3c.py
import streamlit as st
import sys
from pathlib import Path
from streamlit_extras.colored_header import colored_header

# Add the parent directory to sys.path
file_path = Path(__file__).parent.parent
sys.path.insert(0, str(file_path))

# Import config and common_layout
from config_wa import config
from utils.class_wa import wa
from utils.layout_wa import layout_wa


# --- Page configuration ---
st.set_page_config(
    page_title=f"{config.APP_NAME} App",
    page_icon=config.APP_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=config.MENU_ITEMS
)

#colored_header(label="Multi-Agent Framework", description="This is a description", color_name="violet-50")

st.html("""
    <style>
    </style>
    """)


# --- Main page content ---
def left_content():
    st.markdown("### Left Page Content")
    container_left = st.container()
    with container_left:
        st.markdown("Left column content: navigation, links, etc.")
        # Additional left-panel components go here.


def middle_content():
    st.markdown("### Main Page Content")
    container_main = st.container()
    with container_main:
        st.write("This is where your dynamic, page-specific content appears.")
        # Add your charts, forms, or interactive widgets.


def right_content():
    st.write("Right column content: studio tools, details, etc.")
    # Add any extra controls or details specific to this page.

# Build the page using the common layout
layout_wa(left_callback=left_content,
            middle_callback=middle_content,
            right_callback=right_content)

st.markdown("<div style='font-size: 14px; text-align: center; color: gray;'>AI can provide incorrect information. Please verify the answers.</div>", unsafe_allow_html=True)
