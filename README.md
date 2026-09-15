# 🌍 SDG 13: Interactive Climate Action & Environmental Decision Support System

An enterprise-grade modular web application built with **Python** and **Streamlit** to support Sustainable Development Goal 13 (Climate Action).

## 🚀 Key Features

1. **🧱 Enterprise Modular Architecture (`modules/`)**
   - Clean separation of concerns with modular controllers (`chatbot.py`, `footprint.py`, `flood_risk.py`).

2. **🧠 Climate Awareness Chatbot (`modules/chatbot.py`)**
   - Substring intent routing supporting 10 climate topics:
     - Climate Change & Global Warming
     - Carbon Footprint Concepts
     - Emission Reduction Methods
     - Renewable Energy Sources
     - **Methane ($CH_4$) vs. Carbon Dioxide ($CO_2$)**
     - **Deforestation & Nature-based Solutions**
     - **Sea Level Rise & Ocean Warming**
     - **Carbon Offsets & Credits**
     - **SDG 13 Alignment**
   - Quick-prompt button pills for instant user queries.

3. **📊 Carbon Footprint Calculator & Report Exporter (`modules/footprint.py`)**
   - Inputs: Electricity ($0.82 \text{ kg CO}_2/\text{unit}$), Travel ($0.21 \text{ kg CO}_2/\text{km}$), Waste ($0.45 \text{ kg CO}_2/\text{kg}$).
   - **📥 Download Reports**: Features direct export buttons for **CSV** and **Formatted Text (.txt)** summary reports.

4. **🌊 Regional Flood Risk Predictor with Visual Gauge (`modules/flood_risk.py`)**
   - Inputs: Rainfall volume ($mm$), River level ($m$), Soil moisture saturation ($\%$).
   - **🗺️ Interactive Risk Gauge**: Dynamic visual meter indicating threat level from 0% (Low - Green) to 100% (High - Red).
   - Actionable safety protocols and parameter snapshot metrics.

## 🛠️ Installation & Running Locally

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. Open your browser at `http://localhost:8501`.
