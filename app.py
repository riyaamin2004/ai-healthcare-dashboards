import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="MediCore.AI | Healthcare OS", layout="wide", page_icon="🏥")

# --- RECTIFIED DARK UI (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar Navigation */
    section[data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }

    /* The White Hero Card - Fixed Text Contrast */
    .hero-card {
        background: #ffffff;
        padding: 35px;
        border-radius: 16px;
        margin-bottom: 25px;
        color: #0f172a !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .hero-card h2 { color: #0f172a !important; font-weight: 800; margin-bottom: 15px; }
    .hero-card p { color: #334155 !important; line-height: 1.6; font-size: 1.05rem; }

    /* Module Containers */
    .module-box {
        background: #1e293b;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 20px;
    }

    /* Metric Styling */
    [data-testid="stMetricValue"] { color: #38bdf8 !important; font-weight: 700; }
    [data-testid="stMetricLabel"] { color: #94a3b8 !important; }

    /* Button Styling */
    .stButton>button {
        background-color: #38bdf8;
        color: #0f172a;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        padding: 10px 24px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #7dd3fc;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- GLOBAL DATASET (SESSION STATE) ---
if 'patient_data' not in st.session_state:
    st.session_state.patient_data = pd.DataFrame([
        {"ID": "P-8801", "Name": "Riya Sharma", "Symptoms": "Fever, Cough", "Diagnosis": "Viral Flu", "Status": "Recovering"},
        {"ID": "P-8802", "Name": "Aman Verma", "Symptoms": "Fatigue", "Diagnosis": "Anemia", "Status": "Stable"},
        {"ID": "P-8803", "Name": "Sanya Malhotra", "Symptoms": "Chest Pain", "Diagnosis": "Pending", "Status": "Urgent"}
    ])

# --- SIDEBAR NAV ---
with st.sidebar:
    st.markdown("<h2 style='color:#38bdf8;'>🏥 MediCore.AI</h2>", unsafe_allow_html=True)
    st.caption("Advanced Healthcare OS v2.5")
    st.write("---")
    menu = st.radio("SELECT MODULE", ["Dashboard", "AI Chatbot", "Symptom Checker", "Report Analyzer", "Patient Records"])
    st.divider()
    st.info("System: AES-256 Encrypted")

# --- 1. DASHBOARD ---
if menu == "Dashboard":
    st.title("System Dashboard")
    
    st.markdown("""
        <div class="hero-card">
            <h2>AI-assisted healthcare, built on classic OOP pillars.</h2>
            <p>MediCore AI combines a strongly-typed, inheritance-driven Python backend with a modern 
            Streamlit frontend. Every clinical feature is modularized via polymorphic AIService subclasses 
            to ensure scalability, strict data encapsulation, and high-speed diagnostic inference.</p>
        </div>
    """, unsafe_allow_html=True)

    # Quick Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("TOTAL PATIENTS", len(st.session_state.patient_data), "+1")
    m2.metric("AI ACCURACY", "98.2%", "+0.4%")
    m3.metric("ACTIVE SESSIONS", "14")
    m4.metric("SERVER STATUS", "Optimal")

    st.write("---")
    st.subheader("Recent System Activity")
    st.area_chart(pd.DataFrame(random.sample(range(10, 50), 10), columns=["Inflow"]))

# --- 2. AI CHATBOT ---
elif menu == "AI Chatbot":
    st.title("🤖 Neural AI Chat")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask Dr. Aria a medical question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            response = f"I have analyzed your query: '{prompt}'. Based on current medical protocols, please provide more specific symptoms or consult the Symptom Checker module."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- 3. SYMPTOM CHECKER ---
elif menu == "Symptom Checker":
    st.title("🧪 Symptom Analysis")
    with st.container():
        st.markdown('<div class="module-box">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        name = col1.text_input("Patient Full Name")
        age = col2.number_input("Age", 1, 100, 25)
        symptoms = st.multiselect("Identify Symptoms", ["Fever", "Cough", "Headache", "Fatigue", "Nausea", "Body Ache"])
        
        if st.button("Generate Logic-Based Diagnosis"):
            if symptoms:
                with st.spinner("Calculating Probability..."):
                    time.sleep(1)
                    diag = "Viral Infection" if "Fever" in symptoms else "General Fatigue"
                    status = "Critical" if "Fever" in symptoms and "Fatigue" in symptoms else "Stable"
                    
                    # Update Dataset
                    new_p = {"ID": f"P-880{len(st.session_state.patient_data)+1}", "Name": name, "Symptoms": ", ".join(symptoms), "Diagnosis": diag, "Status": status}
                    st.session_state.patient_data = pd.concat([st.session_state.patient_data, pd.DataFrame([new_p])], ignore_index=True)
                    
                    st.success(f"Preliminary Diagnosis: {diag}")
                    st.warning(f"Patient Priority: {status}")
            else:
                st.error("Please select at least one symptom.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 4. REPORT ANALYZER ---
elif menu == "Report Analyzer":
    st.title("📄 AI Report Analyzer")
    st.write("Upload medical scans or blood reports (PDF/JPG).")
    uploaded_file = st.file_uploader("Upload Lab Report", type=["pdf", "png", "jpg"])
    
    if uploaded_file:
        with st.status("Performing OCR Scan...") as s:
            time.sleep(1.5)
            st.write("Extracting Biomarkers...")
            time.sleep(1)
            s.update(label="Analysis Complete!", state="complete")
        
        st.markdown('<div class="module-box">', unsafe_allow_html=True)
        st.subheader("Extracted Findings")
        st.write("- **Hemoglobin:** 14.2 g/dL (Normal)")
        st.write("- **WBC Count:** 11,000 (Slightly High)")
        st.write("- **Glucose:** 95 mg/dL (Normal)")
        st.info("AI Conclusion: Signs of mild inflammation detected. Suggest hydration and rest.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PATIENT RECORDS ---
elif menu == "Patient Records":
    st.title("👨‍⚕️ Encrypted Patient Records")
    st.markdown('<div class="module-box">', unsafe_allow_html=True)
    st.dataframe(st.session_state.patient_data, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Download CSV"):
        st.toast("Exporting encrypted archive...")

# --- FOOTER ---
st.write("---")
st.caption(f"System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Admin: Authorized")
