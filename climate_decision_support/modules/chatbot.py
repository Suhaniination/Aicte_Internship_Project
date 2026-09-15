import streamlit as st

def get_bot_response(user_prompt: str) -> str:
    """Sub-string rule-based intent routing engine for climate queries."""
    user_lower = user_prompt.lower()
    
    if "methane" in user_lower:
        return ("🔥 **Methane (CH₄) vs. Carbon Dioxide (CO₂)**:\n"
                "- Methane is a potent greenhouse gas with a **Global Warming Potential (GWP) 28-36 times higher** than CO₂ over 100 years.\n"
                "- Major sources include agriculture (livestock), landfills, and natural gas leaks.\n"
                "- Reducing methane emissions provides rapid short-term climate cooling benefits!")
        
    elif "deforestation" in user_lower or "forest" in user_lower or "trees" in user_lower:
        return ("🌲 **Deforestation & Climate Impact**:\n"
                "- Forests absorb ~2.6 billion tonnes of CO₂ annually (carbon sinks).\n"
                "- Deforestation accounts for ~10-12% of global greenhouse gas emissions.\n"
                "- Reforestation and protecting natural ecosystems are essential nature-based solutions.")
        
    elif "sea level" in user_lower or "ocean" in user_lower:
        return ("🌊 **Sea Level Rise & Ocean Warming**:\n"
                "- Melting ice sheets/glaciers and thermal expansion of seawater have raised global sea levels by ~20cm since 1900.\n"
                "- Oceans absorb 90% of excess heat trapped by greenhouse gases, leading to ocean acidification and coral bleaching.")
        
    elif "offset" in user_lower or "credit" in user_lower:
        return ("💳 **Carbon Offsets & Credits**:\n"
                "- A carbon offset allows individuals or companies to fund environmental projects (e.g., tree planting, renewable energy) to compensate for their own emissions.\n"
                "- 1 Carbon Credit represents the reduction/removal of **1 Metric Tonne of CO₂**.")
        
    elif "climate change" in user_lower or "global warming" in user_lower:
        return ("🌍 **Climate Change**: Long-term shifts in temperatures and weather patterns, primarily driven by human activities like burning fossil fuels which trap heat in Earth's atmosphere.")
        
    elif "carbon footprint" in user_lower or "footprint" in user_lower:
        return ("👣 **Carbon Footprint**: The total greenhouse gas emissions (CO₂, methane, N₂O) caused directly and indirectly by human activities, products, or organizations.")
        
    elif "how to reduce" in user_lower or "reduce" in user_lower or "sustainable" in user_lower or "save" in user_lower:
        return ("🌱 **Ways to Reduce Emissions**:\n"
                "- **Energy**: Use LED lights, unplug idle devices, install solar panels.\n"
                "- **Transport**: Walk, cycle, use public transit, carpool, or switch to EVs.\n"
                "- **Consumption**: Reduce single-use plastics, compost organic waste, adopt plant-forward diets.")
        
    elif "renewable energy" in user_lower or "clean energy" in user_lower or "solar" in user_lower or "wind" in user_lower:
        return ("☀️ **Renewable Energy**: Energy collected from renewable resources that naturally replenish (Solar, Wind, Hydro, Geothermal, Biomass). Generating clean energy produces zero direct greenhouse gas emissions.")
        
    elif "sdg 13" in user_lower or "sdg" in user_lower or "goal" in user_lower:
        return ("🎯 **SDG 13 (Climate Action)**: Calls for urgent action to combat climate change, strengthen climate resilience, integrate climate policies, and improve climate education globally.")
        
    else:
        return "Sorry, I can help only with climate-related questions (e.g., climate change, carbon footprint, methane, renewable energy, or emission reduction)."


def render_chatbot_module():
    """Renders Module 1: Climate Awareness Chatbot."""
    st.subheader("💬 Climate Change Awareness Chatbot")
    st.markdown("Ask questions about climate change, carbon footprints, renewable energy, or methane emissions.")
    
    # Quick prompt selection
    st.markdown("##### 💡 Suggested Topics:")
    col_q1, col_q2, col_q3, col_q4 = st.columns(4)
    quick_input = None
    
    if col_q1.button("Climate Change"):
        quick_input = "What is climate change?"
    if col_q2.button("Carbon Footprint"):
        quick_input = "What is carbon footprint?"
    if col_q3.button("Methane vs CO₂"):
        quick_input = "What is Methane vs CO₂?"
    if col_q4.button("Renewable Energy"):
        quick_input = "What is renewable energy?"

    # Initialize chat history
    if "climate_messages" not in st.session_state:
        st.session_state.climate_messages = [
            {"role": "assistant", "content": "Hello! I am your Climate Action Assistant. Type your climate-related questions below."}
        ]
        
    for msg in st.session_state.climate_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # Handle user input from chat box or quick prompt buttons
    user_prompt = st.chat_input("Ask a question (e.g., climate change, carbon footprint, methane, renewable energy)...")
    if quick_input:
        user_prompt = quick_input

    if user_prompt:
        st.session_state.climate_messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)
            
        bot_reply = get_bot_response(user_prompt)
            
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
        st.session_state.climate_messages.append({"role": "assistant", "content": bot_reply})
