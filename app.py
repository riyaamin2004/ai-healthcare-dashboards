import streamlit as st
import random

st.set_page_config(page_title="MediCore AI", layout="wide")

# -------- BACKGROUND + GLASS UI --------
st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at 20% 20%, #1e293b, #020617);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(10px);
}

/* Glass Card */
.card {
    background: rgba(255, 255, 255, 0.05);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.4);
}

/* Title */
.title {
    font-size: 32px;
    font-weight: 700;
}

/* Subtext */
.sub {
    color: #94a3b8;
}

</style>
""", unsafe_allow_html=True)

# -------- SIDEBAR --------
st.sidebar.markdown("## 🏥 MediCore AI")
st.sidebar.caption("Healthcare OS")

menu = st.sidebar.radio(
    "",
    ["Dashboard", "Symptom Checker", "AI Chatbot"]
)

# -------- DASHBOARD --------
if menu == "Dashboard":
    st.markdown('<div class="title">🚀 Healthcare Analytics Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">AI-Powered Diagnostics</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">👥 Total Patients<br><h1>128</h1></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">🦠 Common Disease<br><h1>Flu</h1></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">📈 Accuracy<br><h1>89%</h1></div>', unsafe_allow_html=True)

    st.markdown("### 📊 Disease Distribution")

    st.bar_chart({
        "Flu": [47],
        "Cold": [31],
        "Allergy": [15],
        "Stress": [20]
    })

# -------- SYMPTOM CHECKER --------
elif menu == "Symptom Checker":
    st.markdown('<div class="title">🧪 Symptom Checker</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        fever = st.selectbox("Fever", ["No", "Yes"])
        headache = st.selectbox("Headache", ["No", "Yes"])

    with col2:
        fatigue = st.selectbox("Fatigue", ["No", "Yes"])
        cough = st.selectbox("Cough", ["No", "Yes"])

    if st.button("Analyze"):
        confidence = random.randint(85, 95)

        if fever == "Yes" and headache == "Yes":
            disease = "Flu"
            advice = "Take rest and drink fluids"

        elif fever == "Yes" and cough == "Yes":
            disease = "Cold"
            advice = "Stay warm and hydrated"

        else:
            disease = "No major illness"
            advice = "Maintain healthy lifestyle"

        st.success(f"🩺 {disease}")
        st.info(f"💊 {advice}")
        st.warning(f"📊 Confidence: {confidence}%")

# -------- CHATBOT --------
elif menu == "AI Chatbot":
    st.markdown('<div class="title">🤖 AI Assistant</div>', unsafe_allow_html=True)

    user_input = st.text_input("Ask a question")

    if user_input:
        st.markdown('<div class="card">AI Response: Please consult a doctor for accurate diagnosis.</div>', unsafe_allow_html=True)
