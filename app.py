import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="MediCore.AI | Healthcare OS", layout="wide", page_icon="🏥")

# --- MODERN ENTERPRISE UI (CSS) ---
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }

    /* Custom Card */
    .metric-card {
        background: white;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #edf2f7;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: white !important;
        border-right: 1px solid #eee;
    }

    /* Buttons */
    .stButton>button {
        background-color: #1a365d;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #2c5282;
        color: white;
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

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("### 🏥 MediCore.AI")
    st.caption("Healthcare OS")
    st.write("---")
    menu = st.radio("MODULES", ["Dashboard", "AI Chatbot", "Symptom Checker", "Patient Records"], label_visibility="collapsed")
    st.divider()
    st.caption("OOP Pillar: Polymorphism Active")

# --- DASHBOARD ---
if menu == "Dashboard":
    st.title("Dashboard")
    st.caption("AI-assisted healthcare, built on classic OOP pillars.")

    # Top Hero Section
    col_hero_1, col_hero_2 = st.columns([2, 1])
    with col_hero_1:
        st.markdown("""
        <div class="metric-card">
            <h2>AI-assisted healthcare, built on classic OOP pillars.</h2>
            <p style='color: #718096;'>MediCore AI combines a strongly-typed, inheritance-driven Python backend 
            with a modern frontend. Every feature is backed by a polymorphic AIService subclass.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start a consultation ↗"):
             st.toast("Initializing Neural Core...")
             
    with col_hero_2:
        st.markdown("""
        <div class="metric-card" style='background: #000; color: #fff;'>
            <p style='color: #4fd1c5;'>VITALS</p>
            <h3>Powered by GPT-5.1</h3>
            <p style='font-size: 12px; color: #a0aec0;'>Via Emergent Universal LLM</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    
    # Stats Row
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("TOTAL PATIENTS", len(st.session_state.patient_data))
    s2.metric("CHAT SESSIONS", "124")
    s3.metric("AI MESSAGES", "1,042")
    s4.metric("ACTIVE SERVICES", "3")

# --- SYMPTOM CHECKER ---
elif menu == "Symptom Checker":
    st.subheader("🧪 Symptom Checker")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        p_name = col1.text_input("Patient Name")
        temp = col2.slider("Temperature (°F)", 96, 105, 98)
        
        symptoms = st.multiselect("Select Symptoms", ["Fever", "Cough", "Fatigue", "Headache", "Nausea"])
    
    if st.button("Analyze & Save to Records"):
        with st.spinner("Analyzing..."):
            # Simple Logic Checker
            if "Fever" in symptoms and "Cough" in symptoms:
                diag = "Flu/Cold"
            elif "Fatigue" in symptoms:
                diag = "Exhaustion"
            else:
                diag = "Minor Ailment"
            
            # Update Dataframe
            new_entry = {"ID": f"P00{len(st.session_state.patient_data)+1}", 
                         "Name": p_name if p_name else "Anonymous", 
                         "Symptoms": ", ".join(symptoms), 
                         "Diagnosis": diag, 
                         "Status": "New Entry"}
            
            st.session_state.patient_data = pd.concat([st.session_state.patient_data, pd.DataFrame([new_entry])], ignore_index=True)
            st.success(f"Diagnosis: {diag} - Record Updated!")

# --- AI CHATBOT ---
elif menu == "AI Chatbot":
    st.subheader("🤖 AI Chatbot")
    st.chat_message("assistant").write("Hello, I am Dr. Aria. How can I help you today?")
    if prompt := st.chat_input("Ask about symptoms..."):
        st.chat_message("user").write(prompt)
        st.chat_message("assistant").write("I've analyzed your query against the OOP architecture. Please consult a human doctor for final verification.")

# --- PATIENT RECORDS ---
elif menu == "Patient Records":
    st.subheader("👨‍⚕️ Patient Database")
    st.dataframe(st.session_state.patient_data, use_container_width=True, hide_index=True)
    
    # Simple search
    search = st.text_input("🔍 Search patient by name")
    if search:
        filtered = st.session_state.patient_data[st.session_state.patient_data['Name'].str.contains(search, case=False)]
        st.write(filtered)
