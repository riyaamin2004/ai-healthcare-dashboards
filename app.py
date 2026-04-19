import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- SET PAGE CONFIG ---
st.set_page_config(
    page_title="MediCore HUD",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- NEON MEDICAL THEME CSS ---
st.markdown("""
    <style>
    /* Dark Slate Background */
    .stApp {
        background-color: #0a0e14;
        color: #00d4ff;
    }

    /* Glass Panels */
    div[data-testid="stVerticalBlock"] > div.element-container:has(div.med-card) {
        display: block;
    }
    
    .med-card {
        background: rgba(20, 30, 48, 0.6);
        border: 1px solid #00d4ff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.15);
        margin-bottom: 20px;
    }

    /* Text Glow */
    h1, h2, h3 {
        color: #00d4ff !important;
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Custom Button */
    .stButton>button {
        background-color: transparent;
        color: #00d4ff;
        border: 1px solid #00d4ff;
        width: 100%;
        border-radius: 5px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00d4ff;
        color: #0a0e14;
        box-shadow: 0 0 15px #00d4ff;
    }

    /* Metrics Styling */
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP STATE MANAGEMENT ---
if "page" not in st.session_state:
    st.session_state.page = "DASHBOARD"

# --- TOP HUD NAVIGATION BAR ---
st.markdown("<h1 style='text-align: center;'>MEDICORE NEURAL INTERFACE</h1>", unsafe_allow_html=True)
st.write("---")

nav_cols = st.columns(4)
with nav_cols[0]:
    if st.button("📡 SYSTEM DASH"): st.session_state.page = "DASHBOARD"
with nav_cols[1]:
    if st.button("🧪 DIAGNOSTICS"): st.session_state.page = "DIAG"
with nav_cols[2]:
    if st.button("🧠 AI CORE"): st.session_state.page = "AI"
with nav_cols[3]:
    if st.button("📂 ARCHIVES"): st.session_state.page = "DATA"

st.write("")

# --- MODULE 1: DASHBOARD ---
if st.session_state.page == "DASHBOARD":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="med-card">', unsafe_allow_html=True)
        st.subheader("Bio-Telemetry")
        st.metric("Avg Heart Rate", "74 BPM", "Normal")
        st.metric("Critical Alerts", "02", "-1")
        st.metric("Neural Sync", "99.8%", "+0.2%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="med-card">', unsafe_allow_html=True)
        st.subheader("Facility Status")
        st.info("ER Capacity: 84%")
        st.success("Power: Grid Stable")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="med-card">', unsafe_allow_html=True)
        st.subheader("Patient Inflow (24H Cycles)")
        # Using native area chart to avoid ModuleNotFoundError
        chart_data = pd.DataFrame({
            "Time": [f"{i}:00" for i in range(24)],
            "Inpatients": [random.randint(10, 50) for _ in range(24)]
        }).set_index("Time")
        st.area_chart(chart_data, color="#00d4ff")
        st.markdown('</div>', unsafe_allow_html=True)

# --- MODULE 2: DIAGNOSTICS ---
elif st.session_state.page == "DIAG":
    st.markdown('<div class="med-card">', unsafe_allow_html=True)
    st.subheader("Symptom Cross-Reference")
    c1, c2 = st.columns(2)
    with c1:
        symptoms = st.multiselect("Active Biomarkers", ["Pyrexia", "Cephalalgia", "Dyspnea", "Nausea"])
    with c2:
        severity = st.select_slider("Intensity Level", ["LOW", "MODERATE", "ACUTE", "CRITICAL"])
    
    if st.button("RUN NEURAL SCAN"):
        with st.spinner("Analyzing patterns..."):
            st.toast("Scanning Global Medical Database...")
            if "Pyrexia" in symptoms:
                st.error("MATCH FOUND: High probability of Viral Infection.")
            else:
                st.success("NO ACUTE THREATS DETECTED.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- MODULE 3: AI CORE ---
elif st.session_state.page == "AI":
    st.subheader("🧠 Neural Chat Link")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat display
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Query the Neural Core..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            response = f"Neural Core Response: The query '{prompt}' has been analyzed. Based on 2026 clinical protocols, no immediate intervention is required."
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- MODULE 4: ARCHIVES ---
elif st.session_state.page == "DATA":
    st.subheader("📂 Patient Encryption Vault")
    data = pd.DataFrame({
        "Patient ID": ["#9901", "#9902", "#9903"],
        "Registry Name": ["Alpha-Zero", "Beta-One", "Gamma-Nine"],
        "Last Scan": ["2026-04-10", "2026-04-12", "2026-04-15"],
        "Integrity": ["100%", "94%", "98%"]
    })
    st.dataframe(data, use_container_width=True, hide_index=True)

# --- SYSTEM FOOTER ---
st.write("---")
f1, f2, f3 = st.columns(3)
f1.caption(f"SYSTEM TIME: {datetime.now().strftime('%H:%M:%S')}")
f2.caption("SECURITY: AES-512 QUANTUM READY")
f3.caption("USER: ADMIN_CORE_01")
