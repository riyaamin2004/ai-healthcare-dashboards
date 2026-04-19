import streamlit as st
import random
import pandas as pd
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="MediCore AI | Healthcare OS",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR BETTER UI ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    div.stButton > button:first-child {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("# 🏥 MediCore.AI")
    st.caption("Next-Gen Healthcare OS")
    st.divider()
    
    menu = st.selectbox(
        "Navigation",
        ["Dashboard", "Symptom Checker", "AI Chatbot", "Report Analyzer", "Patient Records"],
        index=0
    )
    
    st.sidebar.info("Logged in as: **Dr. Anderson**")
    if st.sidebar.button("Logout"):
        st.toast("Logging out...")

# --- DASHBOARD ---
if menu == "Dashboard":
    st.title("📊 Clinical Dashboard")
    st.markdown(f"**Welcome back.** Today is {datetime.now().strftime('%A, %d %B %Y')}")

    # Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Patients", "142", "+4%")
    m2.metric("Critical Alerts", "3", "-12%")
    m3.metric("Avg. Wait Time", "14 min", "-2m")
    m4.metric("AI Accuracy", "94.2%", "+0.5%")

    st.divider()

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("Patient Inflow Trends")
        chart_data = pd.DataFrame({
            "Time": ["8AM", "10AM", "12PM", "2PM", "4PM", "6PM"],
            "Outpatient": [10, 25, 40, 35, 50, 30],
            "Emergency": [2, 5, 3, 8, 4, 6]
        }).set_index("Time")
        st.area_chart(chart_data)

    with col_right:
        st.subheader("Department Load")
        st.progress(0.85, text="Radiology")
        st.progress(0.40, text="Cardiology")
        st.progress(0.65, text="General Medicine")
        st.progress(0.20, text="Pediatrics")

# --- SYMPTOM CHECKER ---
elif menu == "Symptom Checker":
    st.title("🧪 Diagnostic Assistant")
    st.write("Input symptoms for a preliminary AI assessment.")

    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            fever = st.slider("Body Temperature (°C)", 36.0, 41.0, 37.0, 0.1)
            cough = st.toggle("Persistent Cough")
        with c2:
            duration = st.number_input("Duration of symptoms (Days)", 0, 30)
            fatigue = st.select_slider("Fatigue Level", ["Low", "Moderate", "High", "Extreme"])

    if st.button("Generate Diagnostic Report"):
        with st.spinner("Analyzing medical patterns..."):
            # Logic improvisation
            if fever > 38.5 and cough:
                res, color = "High probability of Viral Infection", "error"
            elif fever > 37.5 and duration > 3:
                res, color = "Mild Infection / Common Cold", "warning"
            else:
                res, color = "No immediate concerns detected", "success"
            
            st.toast("Analysis Complete")
            if color == "error": st.error(res)
            elif color == "warning": st.warning(res)
            else: st.success(res)
            
            st.info("**Recommended Action:** Monitor temperature every 4 hours and maintain hydration.")

# --- AI CHATBOT ---
elif menu == "AI Chatbot":
    st.title("🤖 Medical AI Assistant")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("How can I help you today?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = "I am a simulated AI. In a production app, I would connect to a LLM to answer: " + prompt
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- REPORT ANALYZER ---
elif menu == "Report Analyzer":
    st.title("📄 Smart Report Parser")
    st.info("Upload a PDF or Image of a blood report to extract key biomarkers.")

    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'png', 'jpg'])

    if uploaded_file:
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://via.placeholder.com/400x500.png?text=Scanning+Document...", caption="Analyzing Document")
        with col2:
            st.subheader("Extracted Biomarkers")
            data = {
                "Marker": ["Hemoglobin", "WBC Count", "Glucose", "Cholesterol"],
                "Value": ["14.2 g/dL", "8,500", "95 mg/dL", "180 mg/dL"],
                "Status": ["✅ Normal", "✅ Normal", "✅ Normal", "⚠️ Borderline"]
            }
            st.table(pd.DataFrame(data))

# --- PATIENT RECORDS ---
elif menu == "Patient Records":
    st.title("👨‍⚕️ Digital Health Records")
    
    search = st.text_input("🔍 Search by Name or ID")
    
    records = pd.DataFrame({
        "Patient ID": ["#1021", "#1022", "#1023", "#1024"],
        "Name": ["Riya Sharma", "Aman Verma", "Sarah Jones", "Kevin Hart"],
        "Last Visit": ["2024-05-10", "2024-05-12", "2024-05-14", "2024-05-15"],
        "Diagnosis": ["Influenza", "Common Cold", "Hypertension", "Allergy"],
        "Status": ["Recovered", "Under Treatment", "Stable", "Follow-up"]
    })

    if search:
        records = records[records['Name'].str.contains(search, case=False)]

    st.dataframe(records, use_container_width=True, hide_index=True)
    
    if st.button("➕ Add New Patient"):
        st.write("Redirecting to Patient Intake Form...")
