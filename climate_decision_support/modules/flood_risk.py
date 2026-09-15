import streamlit as st

def render_gauge_meter(risk_level: str, score_percent: float):
    """Renders a visual HTML/CSS hazard gauge meter showing Green -> Orange -> Red level."""
    if risk_level == "HIGH":
        color = "#d32f2f"
        bg_color = "#ffebee"
        label = "CRITICAL THREAT"
    elif risk_level == "MODERATE":
        color = "#ef6c00"
        bg_color = "#fff3e0"
        label = "ELEVATED THREAT"
    else:
        color = "#2e7d32"
        bg_color = "#e8f5e9"
        label = "LOW / NORMAL THREAT"
        
    gauge_html = f"""
    <div style="background-color: {bg_color}; border: 2px solid {color}; border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 20px;">
        <h4 style="margin:0; color: {color}; font-weight: bold; text-transform: uppercase;">Hazard Risk Gauge</h4>
        <div style="margin: 15px 0; background: #e0e0e0; border-radius: 20px; height: 24px; position: relative; overflow: hidden; box-shadow: inset 0 2px 4px rgba(0,0,0,0.15);">
            <div style="width: 100%; height: 100%; background: linear-gradient(90deg, #4caf50 0%, #ff9800 50%, #f44336 100%);"></div>
            <div style="position: absolute; top: 0; left: {score_percent}%; width: 6px; height: 100%; background: #000; border: 1px solid #fff; box-shadow: 0 0 5px rgba(0,0,0,0.5); transform: translateX(-50%);"></div>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 0.8rem; font-weight: bold; color: #555;">
            <span style="color: #2e7d32;">LOW RISK (0%)</span>
            <span style="color: #ef6c00;">MODERATE (50%)</span>
            <span style="color: #d32f2f;">HIGH RISK (100%)</span>
        </div>
        <h2 style="color: {color}; margin-top: 15px; font-weight: 800;">{risk_level} FLOOD RISK ({score_percent:.0f}%)</h2>
        <p style="margin:0; font-size: 0.95rem; color: #444;">Status: <strong>{label}</strong></p>
    </div>
    """
    st.markdown(gauge_html, unsafe_allow_html=True)

def render_flood_risk_module():
    """Renders Module 3: Flood Risk Prediction Assistant with Visual Gauge."""
    st.subheader("🌊 Regional Flood Risk Predictor")
    st.markdown("Evaluate localized flood threat levels based on rainfall volume, river water height, and soil moisture saturation.")
    
    col_f_inputs, col_f_output = st.columns([1, 1], gap="large")
    
    with col_f_inputs:
        st.markdown("### 🌧️ Hydro-Meteorological Inputs")
        rainfall_mm = st.number_input(
            "Enter rainfall (mm):",
            min_value=0.0,
            value=245.0,
            help="Total cumulative rainfall in mm."
        )
        river_level_m = st.number_input(
            "Enter river level (m):",
            min_value=0.0,
            value=15.0,
            help="Current river depth level in meters."
        )
        soil_moisture_percent = st.number_input(
            "Enter soil moisture (%):",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            help="Percentage of soil water capacity currently saturated."
        )
        
        predict_btn = st.button("Predict Flood Risk", type="primary", use_container_width=True)

    with col_f_output:
        st.markdown("### ⚠️ Hazard Assessment Outcome")
        
        # Rule evaluation & visual score computation
        if rainfall_mm > 200 and river_level_m > 8 and soil_moisture_percent > 80:
            risk = "HIGH"
            score = min(100.0, 75.0 + (rainfall_mm - 200)/10.0 + (river_level_m - 8)*2)
            score = min(100.0, score)
            description = "Critical threat! Combination of heavy rainfall, extreme river overflow, and saturated soil."
            advice = "🚨 **Action Protocol**: Issue immediate evacuation warnings for low-lying floodplains. Activate emergency relief centers."
        elif rainfall_mm > 120 and river_level_m > 6:
            risk = "MODERATE"
            score = 50.0 + min(24.0, (rainfall_mm - 120)/10.0 + (river_level_m - 6)*3)
            description = "Substantial threat! Heavy precipitation and elevated river levels detected."
            advice = "⚠️ **Action Protocol**: Alert local safety officers. Prepare drainage clearance and monitor river gauges."
        else:
            risk = "LOW"
            score = min(45.0, (rainfall_mm / 120.0) * 30.0 + (river_level_m / 6.0) * 15.0)
            description = "Normal environmental parameters. No immediate regional flooding threat."
            advice = "✅ **Action Protocol**: Maintain routine meteorological surveillance."

        # Render Visual Gauge Meter
        render_gauge_meter(risk, score)
        
        st.markdown("#### 🛡️ Local Safety Protocol")
        st.write(advice)

    st.markdown("---")
    st.markdown("### 📊 Parameter Visual Snapshot")
    p_col1, p_col2, p_col3 = st.columns(3)
    with p_col1:
        st.metric("Rainfall Volume", f"{rainfall_mm} mm", delta="High Threshold > 200mm" if rainfall_mm > 200 else "Normal")
    with p_col2:
        st.metric("River Level Height", f"{river_level_m} m", delta="High Threshold > 8m" if river_level_m > 8 else "Normal")
    with p_col3:
        st.metric("Soil Saturation", f"{soil_moisture_percent}%", delta="High Saturation > 80%" if soil_moisture_percent > 80 else "Normal")
