import streamlit as st

def render_project_info_module():
    """Renders Module 4: MCA Academic Project Report & SDG 13 documentation."""
    st.subheader("📑 Project Report: Interactive Climate Action & Decision Support System")
    st.markdown("**Course**: Master of Computer Applications (MCA) | **Primary Goal**: UN SDG 13 – Climate Action")
    st.markdown("---")
    
    st.markdown("""
    ### 1. Executive Overview & Objectives
    Climate change introduces compounding environmental vulnerabilities ranging from volatile carbon emissions to extreme weather hazards like regional flooding. 
    This system provides a lightweight, real-time, interactive decision support web application built with **Python and Streamlit** to deliver:
    - **Module 1: Climate Awareness Chatbot**: Conversational rule-based intent routing supporting 10 climate domains.
    - **Module 2: Carbon Footprint Calculation Tool**: Metric evaluations ($0.82 \\text{ kg CO}_2/\\text{unit}$ electricity, $0.21 \\text{ kg CO}_2/\\text{km}$ travel, $0.45 \\text{ kg CO}_2/\\text{kg}$ waste) with downloadable CSV/TXT reports.
    - **Module 3: Flood Risk Prediction Assistant**: Multi-parameter hydro-meteorological threshold rules with an interactive hazard gauge meter.

    ### 2. Core Research Question
    > *How can an interactive web-based decision support system empower users with real-time carbon tracking, disaster risk evaluation, and climate awareness education?*

    ### 3. System Architecture & Mathematical Engine
    
    #### A. Carbon Footprint Formula
    $$\\text{Total Monthly Emission (kg CO}_2) = (\\text{Electricity} \\times 0.82) + (\\text{Travel} \\times 0.21) + (\\text{Waste} \\times 0.45)$$

    #### B. Flood Threat Classification Matrix
    | Threat Level | Rainfall ($mm$) | River Level ($m$) | Soil Saturation ($\\%$) | Action Protocol |
    | :--- | :--- | :--- | :--- | :--- |
    | **HIGH** | $> 200 \\text{ mm}$ | $> 8.0 \\text{ m}$ | $> 80\\%$ | Issue immediate evacuation warnings |
    | **MODERATE** | $> 120 \\text{ mm}$ | $> 6.0 \\text{ m}$ | Any | Alert local safety officers & monitor gauges |
    | **LOW** | $\\le 120 \\text{ mm}$ | $\\le 6.0 \\text{ m}$ | Any | Maintain routine surveillance |

    ### 4. Technical Stack & Modular Architecture
    - **Language**: Python 3.x
    - **Web Framework**: Streamlit
    - **Data Processing & Export**: Pandas, CSV, Text
    - **Modular Packages**: `modules/chatbot.py`, `modules/footprint.py`, `modules/flood_risk.py`, `modules/project_info.py`
    """)
