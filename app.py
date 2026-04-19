import streamlit as st
import random

st.set_page_config(page_title="MediCore AI", layout="wide")

# -------- SIDEBAR --------
st.sidebar.markdown("## 🏥 MediCore.AI")
st.sidebar.caption("Healthcare OS")

menu = st.sidebar.radio(
    "Modules",
    ["Dashboard", "Symptom Checker", "AI Chatbot", "Report Analyzer", "Patient Records"]
)

# -------- DASHBOARD --------
if menu == "Dashboard":
    st.title("📊 MediCore AI Dashboard")
    st.markdown("### AI-assisted healthcare system")

    col1, col2, col3 = st.columns(3)

    col1.metric("Patients", "120")
    col2.metric("Common Disease", "Flu")
    col3.metric("Accuracy", "87%")

    st.markdown("---")
    st.subheader("System Overview")

    st.write("This system simulates AI-based healthcare using rule-based logic.")

    st.bar_chart({
        "Flu": [12],
        "Cold": [19],
        "Allergy": [7],
        "Stress": [10]
    })

# -------- SYMPTOM CHECKER --------
elif menu == "Symptom Checker":
    st.title("🧪 Symptom Checker")

    col1, col2 = st.columns(2)

    with col1:
        fever = st.selectbox("Fever", ["No", "Yes"])
        headache = st.selectbox("Headache", ["No", "Yes"])

    with col2:
        fatigue = st.selectbox("Fatigue", ["No", "Yes"])
        cough = st.selectbox("Cough", ["No", "Yes"])

    if st.button("Analyze Symptoms"):
        confidence = random.randint(80, 95)

        if fever == "Yes" and headache == "Yes":
            disease = "Flu"
            advice = "Take rest and drink fluids"

        elif fever == "Yes" and cough == "Yes":
            disease = "Cold"
            advice = "Stay warm and hydrated"

        else:
            disease = "No major illness"
            advice = "Stay healthy"

        st.success(f"Diagnosis: {disease}")
        st.info(f"Advice: {advice}")
        st.warning(f"Confidence: {confidence}%")

# -------- AI CHATBOT --------
elif menu == "AI Chatbot":
    st.title("🤖 AI Chatbot")

    user_input = st.text_input("Ask a health question:")

    if user_input:
        st.write("AI Response:")
        st.success("Based on your query, please consult a doctor for accurate diagnosis.")

# -------- REPORT ANALYZER --------
elif menu == "Report Analyzer":
    st.title("📄 Report Analyzer")

    file = st.file_uploader("Upload medical report")

    if file:
        st.success("Report uploaded successfully!")
        st.info("Basic analysis: No critical issues detected.")

# -------- PATIENT RECORDS --------
elif menu == "Patient Records":
    st.title("👨‍⚕️ Patient Records")

    st.write("Sample Records:")
    st.table({
        "Name": ["Riya", "Aman"],
        "Disease": ["Flu", "Cold"],
        "Status": ["Recovering", "Stable"]
    })
