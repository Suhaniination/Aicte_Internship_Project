import streamlit as st

# Import modular application components
from modules.chatbot import render_chatbot_module
from modules.footprint import render_footprint_module
from modules.flood_risk import render_flood_risk_module

# Page Configuration
st.set_page_config(
    page_title="SDG 13: Climate Action Assistant",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Application Main Header
st.markdown("<h1 style='text-align: center; color: #2E7D32; font-weight: 700; margin-bottom: 5px;'>🌍 SDG 13: Climate Action Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555; font-size: 1.1rem; margin-bottom: 20px;'>Interactive Climate Action & Environmental Decision Support System</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar Navigation & Metadata
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/earth-planet.png", width=70)
    st.title("Navigation")
    
    tool_mode = st.radio(
        "Select Climate Tool Module:",
        [
            "💬 Climate Awareness Chatbot",
            "📊 Carbon Footprint Calculator",
            "🌊 Regional Flood Risk Predictor"
        ]
    )
    
    st.markdown("---")
    st.markdown("### 🎯 Goal Alignment")
    st.info("**SDG 13**: Take urgent action to combat climate change and its impacts.")

# Route to corresponding module view
if "💬 Climate Awareness Chatbot" in tool_mode:
    render_chatbot_module()

elif "📊 Carbon Footprint Calculator" in tool_mode:
    render_footprint_module()

elif "🌊 Regional Flood Risk Predictor" in tool_mode:
    render_flood_risk_module()
