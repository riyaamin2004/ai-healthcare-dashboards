import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- SET PAGE CONFIG ---
st.set_page_config(
    page_title="MediCore AI | Premium",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- LUXURY UI THEMING ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Custom Card Styling */
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #eef2f6;
        text-align: center;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #1e293b;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Button Styling */
    .stButton>button {
        border-radius: 8px;
        transition: all 0.3s ease;
        background-color: #0ea5e9;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(14, 165, 233, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/387/387561.png", width=80)
    st.markdown("## MediCore AI")
    st.caption("Clinical Intelligence OS v2.0")
    st.divider()
    
    menu = st.radio(
        "NAVIGATION",
        ["System Dashboard", "Symptom Analysis", "Medical Chatbot", "Lab Analyzer", "Patient Database"],
        label_visibility="collapsed"
    )
    
    st.spacer = st.empty()
    st.divider()
    st.info("System Status: **Operational**")

# --- DASHBOARD MODULE ---
if menu == "System Dashboard":
    st.title("📊 Clinical Overview")
    st.markdown("Real-time telemetry and patient distribution.")

    # Top Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Total Patients", "1,284", "+12%")
        st.markdown('</div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Consultations", "48", "Active")
        st.markdown('</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Avg Diagnosis Time", "4.2m", "-15s")
        st.markdown('</div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("System Accuracy", "96.4%", "+0.2%")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Disease Prevalence")
    chart_data = pd.DataFrame({
        "Condition": ["Influenza", "Type 2 Diabetes", "Hypertension", "Allergies", "Fatigue"],
        "Case Count": [45, 32, 56, 21, 15]
    })
    st.bar_chart(chart_data, x="Condition", y="Case Count", color="#0ea5e9")

# --- SYMPTOM ANALYSIS ---
elif menu == "Symptom Analysis":
    st.title("🧪 Smart Diagnostics")
    
    with st.expander("Patient Demographics", expanded=True):
        c1, c2, c3 = st.columns(3)
        age = c1.number_input("Age", 0, 120, 25)
        gender = c2.selectbox("Gender", ["Male", "Female", "Other"])
        blood_group = c3.selectbox("Blood Group", ["A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"])

    st.subheader("Current Symptoms")
    symptoms = st.multiselect(
        "Select all that apply:",
        ["High Fever", "Dry Cough", "Chest Pain", "Shortness of Breath", "Fatigue", "Headache", "Loss of Taste"]
    )
    
    severity = st.select_slider("Symptom Severity", options=["Mild", "Moderate", "Severe", "Critical"])

    if st.button("Run AI Diagnostic"):
        with st.status("Analyzing medical databases...", expanded=True) as status:
            time.sleep(1)
            st.write("Cross-referencing symptoms...")
            time.sleep(1)
            st.write("Calculating confidence scores...")
            status.update(label="Analysis Complete!", state="complete", expanded=False)
        
        if "High Fever" in symptoms and "Dry Cough" in symptoms:
            st.error("### Potential Finding: Viral Respiratory Infection")
            st.warning("**Recommendation:** Immediate PCR test and self-isolation.")
        else:
            st.success("### Finding: No Critical Patterns Detected")
            st.info("General wellness advised. Increase fluid intake.")

# --- MEDICAL CHATBOT ---
elif menu == "Medical Chatbot":
    st.title("🤖 MediCore AI Assistant")
    st.caption("Ask questions about medications, symptoms, or general health.")

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is the dosage for Paracetamol?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Mocking a smart response
            response = f"Based on medical guidelines, your query regarding '{prompt}' requires professional verification, but generally..."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- LAB ANALYZER ---
elif menu == "Lab Analyzer":
    st.title("📄 Lab Report Intelligence")
    
    uploaded_file = st.file_uploader("Drop medical PDF or Image here", type=["pdf", "png", "jpg"])
    
    if uploaded_file:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.success("File Uploaded!")
            st.image("https://via.placeholder.com/300x400.png?text=Report+Preview", use_container_width=True)
        with col2:
            st.subheader("Detected Values")
            results = pd.DataFrame({
                "Metric": ["Glucose", "HbA1c", "HDL", "LDL"],
                "Result": [110, 5.7, 45, 120],
                "Range": ["70-100", "< 5.7", "> 40", "< 100"],
                "Status": ["High", "Normal", "Normal", "High"]
            })
            st.table(results)
            st.toast("Anomalies detected in Glucose and LDL", icon="⚠️")

# --- PATIENT DATABASE ---
elif menu == "Patient Database":
    st.title("👨‍⚕️ Patient Record Management")
    
    # Mock Data
    data = {
        "ID": ["PX-001", "PX-002", "PX-003", "PX-004", "PX-005"],
        "Patient Name": ["Alice Smith", "Bob Johnson", "Charlie Davis", "Diana Prince", "Edward Norton"],
        "Last Checkup": ["2024-03-01", "2024-03-15", "2024-04-02", "2024-04-10", "2024-04-18"],
        "Primary Doctor": ["Dr. House", "Dr. Strange", "Dr. Grey", "Dr. Watson", "Dr. Brown"],
        "Priority": ["Medium", "High", "Low", "Critical", "Medium"]
    }
    df = pd.DataFrame(data)

    # Search Bar
    search = st.text_input("Search Patient Registry", placeholder="Enter name or ID...")
    if search:
        df = df[df['Patient Name'].str.contains(search, case=False)]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Priority": st.column_config.SelectboxColumn(
                "Priority",
                options=["Low", "Medium", "High", "Critical"],
            ),
            "Last Checkup": st.column_config.DateColumn("Last Checkup")
        }
    )
    
    st.button("➕ Register New Patient")
