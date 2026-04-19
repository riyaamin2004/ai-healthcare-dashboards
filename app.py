import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- CORE CONFIG ---
st.set_page_config(page_title="MediCore HUD", layout="wide", page_icon="🧬")

# --- CYBER-MEDICINE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

    /* Global Style */
    .stApp {
        background-color: #050b14;
        color: #00f2ff;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Glass Panels */
    .med-panel {
        background: rgba(16, 25, 45, 0.7);
        border: 1px solid #00f2ff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2);
        margin-bottom: 20px;
    }

    /* Header Styling */
    .hud-title {
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 5px;
        color: #00f2ff;
        text-shadow: 0 0 10px #00f2ff;
        margin-bottom: 30px;
    }

    /* Metric Styling */
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 2rem !important;
    }
    
    /* Hide Default UI elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- TOP HUD NAVIGATION ---
st.markdown("<h1 class='hud-title'>MediCore HUD v3.0</h1>", unsafe_allow_html=True)

nav_cols = st.columns(5)
with nav_cols[0]:
    if st.button("📡 SYSTEM"): st.session_state.page = "Dashboard"
with nav_cols[1]:
    if st.button("🧪 ANALYSIS"): st.session_state.page = "Analysis"
with nav_cols[2]:
    if st.button("🧠 NEURAL AI"): st.session_state.page = "AI"
with nav_cols[3]:
    if st.button("📂 ARCHIVE"): st.session_state.page = "Records"
with nav_cols[4]:
    if st.button("⚙️ SETTINGS"): st.toast("System Preferences Locked.")

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# --- DASHBOARD PAGE ---
if st.session_state.page == "Dashboard":
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="med-panel">', unsafe_allow_html=True)
        st.subheader("Vital Statistics")
        st.metric("Heart Rate Avg", "72 BPM", "Normal")
        st.metric("O2 Saturation", "98%", "Optimal")
        st.metric("Patient Load", "14 Active", "+2")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="med-panel">', unsafe_allow_html=True)
        st.subheader("System Alerts")
        st.error("⚠️ Bed 04: BP Spike Detected")
        st.warning("⚡ AI Core: Updates Pending")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="med-panel">', unsafe_allow_html=True)
        st.subheader("Biometric Activity (24H)")
        # Create a neon-style plot
        df = pd.DataFrame({
            'Time': list(range(24)),
            'Inflow': [10, 8, 5, 2, 4, 12, 18, 25, 30, 22, 19, 21, 25, 28, 35, 40, 38, 30, 25, 20, 15, 12, 10, 9]
        })
        fig = px.area(df, x='Time', y='Inflow', template="plotly_dark")
        fig.update_traces(line_color='#00f2ff', fillcolor='rgba(0, 242, 255, 0.1)')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- NEURAL AI PAGE ---
elif st.session_state.page == "AI":
    st.subheader("🧠 Neural Interaction Core")
    
    st.markdown('<div class="med-panel">', unsafe_allow_html=True)
    st.info("Direct Link established with Gemini 3 Flash. AI is ready to analyze clinical queries.")
    
    chat_container = st.container(height=400)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for m in st.session_state.messages:
        with chat_container.chat_message(m["role"]):
            st.write(m["content"])

    if prompt := st.chat_input("Input Medical Query..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_container.chat_message("user"):
            st.write(prompt)
        
        with chat_container.chat_message("assistant"):
            response = f"Simulating Diagnosis for: {prompt}. Analysis complete. No abnormalities detected."
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown('</div>', unsafe_allow_html=True)

# --- ANALYSIS PAGE ---
elif st.session_state.page == "Analysis":
    st.subheader("🧪 Molecular Analysis")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="med-panel">', unsafe_allow_html=True)
        symptom_list = st.multiselect("Input Detected Symptoms", ["Pyrexia", "Dyspnea", "Tachycardia", "Cephalalgia"])
        confidence = st.slider("Required Confidence Threshold", 0, 100, 85)
        if st.button("RUN SCAN"):
            st.write("Processing DNA Markers...")
            st.progress(100)
            st.success("Result: Negative for common pathogens.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:
        st.markdown('<div class="med-panel">', unsafe_allow_html=True)
        st.subheader("Protein Mapping")
        # Radar chart for fun
        categories = ['Cell Affinity', 'Pathogen Resist', 'Metabolism', 'Immunity']
        fig = go.Figure(data=go.Scatterpolar(
            r=[80, 50, 70, 90],
            theta=categories,
            fill='toself',
            marker=dict(color='#00f2ff')
        ))
        fig.update_layout(polar=dict(bgcolor='rgba(0,0,0,0)'), paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER DATA ---
st.divider()
f_col1, f_col2, f_col3 = st.columns(3)
with f_col1: st.caption("LOG: Patient records synced.")
with f_col2: st.caption("UTC: " + datetime.now().strftime("%H:%M:%S"))
with f_col3: st.caption("ENCRYPTION: AES-256 ACTIVE")
