# Classes
import streamlit as st
import os
from pathlib import Path

class wa:
    # Add vertical space
    @staticmethod
    def wa_spacer(height):
        st.markdown(f'<div style="height: {height}px;"></div>', unsafe_allow_html=True)

    def __init__(self):
        pass
