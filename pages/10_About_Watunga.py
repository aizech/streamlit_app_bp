import streamlit as st
import os
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
#st.markdown("# Contact")

st.markdown("""
# The Watunga Framework

## Assistants vs. Agents

The difference between assistants and agents
- **AI Assistants** are tools that assist humans in tasks, usually reactive and responsive to user requests. They execute commands, provide information and help with decisions (e.g. ChatGPT, Siri).
- **AI Agents** act more autonomously, pursue their own goals and perform complex tasks, often without constant user interaction. They learn and react dynamically to environmental changes (e.g. autonomous robots or trading algorithms).



## The Watunga Basic Components

### 🤖 Agents

Agents are autonomous units in the framework that are specialized to perform specific tasks. Each agent has a specific goal and has the ability to interact with other agents or tools. Agents can process information, make decisions, and perform actions based on their mandate.

### 🛠️ Tools

Tools are specialized tools used by agents to perform their tasks. A tool is a module that provides a specific function, such as retrieving data, performing calculations, or communicating with APIs. Each tool is implemented in Python and contains a defined runmethod where the actual logic is executed. Tools are usually reusable and can be used by multiple agents.

### 🔅 Agencies

An agency is a group of agents working together to achieve a common goal. Each agency specializes in a specific task or business process. Within an agency, the roles of the agents are clearly defined and they work together in a coordinated manner to achieve the overall goal. Agents within an agency can share tools and learn from each other.

### 🌱 Genesis

Genesis describes the process by which new agents or agencies are created. It is the starting point for every new unit in the Watunga Framework. Genesis determines the basic structure and behavior of the agents by defining certain parameters, such as the tasks of the agents and the tools used.
Genesis can independently access existing agents and tools and existing agencies. It combines these to create new agents and agencies. If an agent or tool is not available, Genesis develops and tests the missing components itself.
Genesis is an AI agency that develops other AI agents and is constantly learning.

## 🧙‍♂️ Agents use tools

Agents use tools to perform their tasks. They can access external APIs, analyze data, or perform specific operations to complete a task. The focus is on allowing agents to act autonomously, but extend their functionality through tools and collaboration with other agents.

Example:

- An agent is given the task of retrieving weather data.  
- The agent uses a tool that uses an API to extract the weather data.  
- The agent then processes the data and passes it on to another agent, which further processes or stores it.

## :material/partner_exchange: Collaboration of Agents 

The framework enables users to automate complex tasks by leveraging a "swarm" intelligence of specialized agents. The main goal is to simplify work by eliminating the need for humans to perform each task themselves, but instead letting specialized agents and tools do it for them.

""")

st.markdown("---")

one_col = st.columns([1])[0]
with one_col:
    col1, col2 = st.columns([1, 4])

    with col1:
        st.image(logo_icon_path, use_container_width=True)

    with col2:
        st.markdown("""
    **Watunga** - *noun, masculine [Swahili]*

    **Definition:**

    1. (plural) builder, creator, designer
    2. People who create or design something, especially in connection with the construction or creation of physical or abstract objects.

    **Origin:** Derived from the Swahili verb root “-tunga,” meaning “to create” or “to form.”

    **Watunga** literally means “the builders” or “the creators” (in the plural), where “wa-” indicates the plural of persons and “-tunga” denotes the act of creation.
        """, unsafe_allow_html=True)

st.markdown("Made with :material/favorite: by [Watunga](https://www.watunga.com/)")