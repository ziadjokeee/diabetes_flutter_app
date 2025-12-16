import streamlit as st
import numpy as np
import pickle
 
# ---------------- SESSION STATE (TOGGLE) ----------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True
 
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="centered"
)
 
# ---------------- THEME TOGGLE ----------------
st.toggle("🌙 Dark Mode", key="dark_mode")
 
if st.session_state.dark_mode:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
 
# ---------------- LOAD MODEL ----------------
model = pickle.load(open("diabetes_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
 
# ---------------- TITLE ----------------
st.title("🩺 Diabetes Progression Prediction")
st.subheader("Machine Learning Based Prediction System")
 
st.markdown(
    """
    This application predicts the **diabetes progression score** using a
    trained **machine learning regression model**.
 
    ℹ️ **All inputs are standardized**
    - `0` → average patient  
    - positive values → above average  
    - negative values → below average
    """
)
 
st.divider()
 
# ---------------- INPUT SECTION ----------------
st.header("📋 Patient Data")
 
col1, col2 = st.columns(2)
 
with col1:
    age = st.slider("📅 Age (normalized)", -0.1, 0.1, 0.0)
    sex = st.slider("⚥ Sex (normalized)", -0.1, 0.1, 0.0)
    bmi = st.slider("⚖️ BMI (normalized)", -0.2, 0.2, 0.05)
    bp  = st.slider("💓 Blood Pressure (normalized)", -0.2, 0.2, 0.03)
    s1  = st.slider("🧪 Total Cholesterol (S1)", -0.2, 0.2, 0.02)
 
with col2:
    s2 = st.slider("🧬 LDL Cholesterol (S2)", -0.2, 0.2, 0.01)
    s3 = st.slider("🛡️ HDL Cholesterol (S3)", -0.2, 0.2, -0.02)
    s4 = st.slider("📊 Cholesterol Ratio (S4)", -0.2, 0.2, 0.02)
    s5 = st.slider("🍬 Triglycerides (S5)", -0.2, 0.2, 0.04)
    s6 = st.slider("🧁 Glucose (S6)", -0.2, 0.2, 0.01)
 
st.divider()
 
# ---------------- PREDICTION ----------------
if st.button("🔍 Predict Diabetes Progression"):
 
    input_data = np.array([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
 
    # Risk interpretation
    if prediction < 150:
        risk = "🟢 Low progression risk"
    elif prediction < 250:
        risk = "🟡 Moderate progression risk"
    else:
        risk = "🔴 High progression risk"
 
    st.success("Prediction completed successfully!")
 
    st.metric(
        label="Predicted Diabetes Progression Score",
        value=f"{prediction:.2f}"
    )
 
    st.write("### Risk Interpretation")
    st.write(risk)
 
# ---------------- FOOTER ----------------
st.divider()
st.caption(
    "⚠️ This application is for **educational purposes only** "
    "and must not be used for medical diagnosis."
)