import streamlit as st
from pathlib import Path

class Config:
    # --- Constants & Directories ---
    APP_NAME      = "Watunga"
    APP_ICON      = "🤖"
    APP_URL       = "https://www.watunga.com"
    CONTACT_EMAIL = "ai@zechmann.de"

    THIS_DIR      = Path(__file__).parent
    STYLES_DIR    = THIS_DIR / "styles"
    CSS_FILE      = STYLES_DIR / "main.css"
    ASSETS_DIR    = THIS_DIR / "assets"

    MENU_ITEMS = {
        'Get Help': f"{APP_URL}/help",
        'Report a bug': f"{APP_URL}/bug",
        'About': "## This is a header. This is an *extremely* cool " + APP_NAME + " app!"
    }

# Create a single instance to be imported by other modules
config = Config()
