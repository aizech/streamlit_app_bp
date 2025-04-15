# Page: Template_Page_3c.py
import streamlit as st
import sys
import os
from pathlib import Path
from streamlit_extras.colored_header import colored_header

# Add the parent directory to sys.path
file_path = Path(__file__).parent.parent
sys.path.insert(0, str(file_path))

# Import config and common_layout
from config_wa import config
from utils.class_wa import wa
from utils.layout_wa import layout_wa
from utils.layout_simple_wa import layout_simple_wa


# --- Page configuration ---
st.set_page_config(
    page_title=f"{config.APP_NAME} App",
    page_icon=config.APP_ICON,
    layout="wide",
    #initial_sidebar_state="collapsed",
    menu_items=config.MENU_ITEMS
)

# --- Logo ---
logo_text_path = os.path.join(config.ASSETS_DIR, "logo_text.png")
logo_icon_path = os.path.join(config.ASSETS_DIR, "logo.png")

st.logo(logo_text_path,
    size="small",
    #link="https://www.watunga.com/",
    icon_image=logo_icon_path
)

#colored_header(label="Multi-Agent Framework", description="This is a description", color_name="violet-50")

st.html("""
    <style>
    </style>
    """)

# --- Main page content ---
def simple_content():
    st.markdown("### Simple Page Content")
    container_main = st.container()
    with container_main:
        st.write("This is where your dynamic, page-specific content appears.")
        # Add your charts, forms, or interactive widgets.

def left_column():
    st.markdown(":material/chat: :grey[Chat]")

def middle_column():
    st.markdown(":material/insert_chart: :grey[Charts]")

def right_column():
    st.markdown(":material/info: :grey[Info]")

# Build the page using the common layout
layout_simple_wa(main_callback=simple_content, left_callback=left_column, middle_callback=None, right_callback=None)


st.markdown("<div style='font-size: 14px; text-align: center; color: gray;'>AI can provide incorrect information. Please verify the answers.</div>", unsafe_allow_html=True)
