import streamlit as st
import os
from streamlit_extras.colored_header import colored_header
from pathlib import Path

from config_wa import config
from utils.class_wa import wa
from utils.layout_wa import layout_wa

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
    size="medium",
    #link="https://www.watunga.com/",
    icon_image=logo_icon_path
)

# --- Content ---
st.markdown("""
# The AI Multi Agent Framework
## :material/potted_plant: Mission

We will create an AI-Multi-Agent-Framework for an AI-Fabric with reusable AI-Agents and reusable Tools. 
And we will develop a Creation Tool for creating, assembling and reusing AI-Agents and Tools (Genesis).


## :material/rocket_launch: Our Mission
We believe that the future of work lies in the collaboration between humans and machines. Our AI platform and agents are designed to optimize business processes, scale automation, and relieve teams so they can focus on strategic decisions.

## :material/star: Our Vision
We strive to fundamentally change the way how Bertrandt works. By leveraging our innovative AI platform technologies, we aim to increase productivity and maximize efficiency. We shape the future of humans and AI.

## :material/settings_heart: Our Technology
We offer a flexible and customizable AI infrastructure. Our agents and tools are individually designed and can be seamlessly integrated into existing ecosystems. Whether for small businesses or large corporations, we have the right solution for every challenge. Our AI platform is built as a self-learning system. The system learns itself with every project, process, agency, agent and tools we create. Therefore, our innovative platform is extremely flexible, scalable and secure for enterprise usage.

""")

wa.wa_spacer(50)

one_col = st.columns([1])[0]
with one_col:
    col1, col2 = st.columns([1, 4])

    with col1:
        st.image(f"{config.ASSETS_DIR}/logo.png", use_container_width=True)

    with col2:
        st.markdown("""
    **Watunga** - *noun, masculine [Swahili]*

    **Definition:**

    1. (plural) builder, creator, designer
    2. People who create or design something, especially in connection with the construction or creation of physical or abstract objects.

    **Origin:** Derived from the Swahili verb root “-tunga,” meaning “to create” or “to form.”

    **Watunga** literally means “the builders” or “the creators” (in the plural), where “wa-” indicates the plural of persons and “-tunga” denotes the act of creation.
        """, unsafe_allow_html=True)

wa.wa_spacer(50)

st.markdown("Made with :material/favorite: by [Watunga](https://www.watunga.com/)")
