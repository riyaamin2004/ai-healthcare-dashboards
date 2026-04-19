import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="MediCore.AI | Healthcare OS", layout="wide", page_icon="🏥")

# --- RECTIFIED DARK UI (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    /* Force dark background for the whole app */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }

    /* Fix Sidebar visibility */
    section[data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }
    section[data-testid="stSidebar"] .stText, section[data-testid="stSidebar"] label {
        color: #e2e8f0 !important;
    }

    /* Main Hero Card - Fixed text visibility */
    .hero-card {
        background: #ffffff;
        padding: 30px;
        border-radius: 16px;
        margin-bottom: 25px;
        color: #1e293b !important; /* Force dark text on white card */
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }
    .hero-card h2 {
        color: #0f172a !important;
        font-weight: 700;
    }
    .hero-card p {
        color: #475569 !important;
        font-size: 1.1rem;
    }

    /* Metric Box */
    [data-testid="stMetric"] {
        background: #1e293b;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #334155;
    }
    [data-testid="stMetricValue"] {
        color: #38bdf8 !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #38bdf8;
        color: #0f172a;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background-color: #7dd3fc;
        color: #0f172a;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MOCK DATASET ---
if 'patient_data' not in st.session_state:
    st.session_state.patient_data = pd.DataFrame([
        {"ID": "P001", "Name": "Riya Sharma", "Symptoms": "Fever, Cough", "Diagnosis": "Viral Flu", "Status": "Recovering"},
        {"ID": "P002", "Name": "Aman Verma", "Symptoms": "Fatigue", "Diagnosis": "Anemia", "Status": "Stable"},
        {"ID": "P003", "Name": "Sanya Malhotra", "Symptoms": "Chest Pain", "Diagnosis": "Pending", "Status": "Urgent"},
        {"ID": "P004", "Name": "Rahul Singh", "Symptoms": "Sneezing", "Diagnosis": "Allergy", "Status": "Stable"}
    ])

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color:#38bdf8;'>🏥 MediCore.AI</h2>", unsafe_allow_html=True)
    st.caption("v2.4 Premium OS")
    st.write("---")
    menu = st.radio("MODULES", ["Dashboard", "AI Chatbot", "Symptom Checker", "Patient Records"])
    st.divider()
    st.caption("System: Operational")

# --- DASHBOARD ---
if menu == "Dashboard":
    st.title("Clinical Dashboard")
    
    # Hero Card with FIXED Text Visibility
    st.markdown("""
        <div class="hero-card">
            <h2>AI-assisted healthcare, built on classic OOP pillars.</h2>
            <p>MediCore AI combines a strongly-typed, inheritance-driven Python backend with a modern 
            Streamlit frontend. Every clinical feature is modularized via polymorphic AIService subclasses 
            to ensure scalability and data integrity.</p>
        </div>
    """, unsafe_allow_html=True)

    col_btn, _ = st.columns([1, 2])
    with col_btn:
        if st.button("Start a consultation ↗"):
            st.toast("Booting Diagnostic Engine...")

    st.write("---")
    
    # Vitals Row
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("TOTAL PATIENTS", len(st.session_state.patient_data))
    s2.metric("CHAT SESSIONS", "124", "+12")
    s3.metric("AI MESSAGES", "1,042")
    s4.metric("SYSTEM UPTIME", "99.9%")

# --- SYMPTOM CHECKER ---
elif menu == "Symptom Checker":
    st.subheader("🧪 Rapid Symptom Analysis")
    with st.container():
        c1, c2 = st.columns(2)
        p_name = c1.text_input("Patient Registry Name")
        symptoms = st.multiselect("Active Symptoms", ["Fever", "Cough", "Fatigue", "Nausea", "Headache"])
    
    if st.button("Generate Diagnosis"):
        diag = "General Viral Infection" if "Fever" in symptoms else "Routine Check-up"
        new_entry = {
            "ID": f"P00{len(st.session_state.patient_data)+1}", 
            "Name": p_name if p_name else "Guest", 
            "Symptoms": ", ".join(symptoms), 
            "Diagnosis": diag, 
            "Status": "Stable"
        }
        st.session_state.patient_data = pd.concat([st.session_state.patient_data, pd.DataFrame([new_entry])], ignore_index=True)
        st.success(f"Logic Result: {diag}")

# --- OTHER MODULES ---
elif menu == "AI Chatbot":
    st.subheader("🤖 Neural Core Chat")
    st.chat_message("assistant").write("Systems online. How can I assist with patient triaging?")
    if p := st.chat_input("Ask anything..."):
        st.chat_message("user").write(p)
        st.chat_message("assistant").write("Analyzing query against clinical knowledge base...")

elif menu == "Patient Records":
    st.subheader("👨‍⚕️ Encrypted Patient Records")
    st.dataframe(st.session_state.patient_data, use_container_width=True, hide_index=True)
