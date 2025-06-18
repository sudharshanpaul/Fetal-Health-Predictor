import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load preprocessor and model
with open("models/preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)

with open("models/random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# Mapping for dropdown options
categorical_dropdowns = {
    "severe_decelerations": [0.000, 0.001],
    "prolongued_decelerations": [0.000, 0.001, 0.002, 0.003, 0.004, 0.005],
    "histogram_number_of_zeroes": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 7.0, 8.0, 10.0],
    "histogram_tendency": [-1.0, 0.0, 1.0]
}

# All input features
feature_names = [
    "baseline value",
    "accelerations",
    "fetal_movement",
    "uterine_contractions",
    "light_decelerations",
    "severe_decelerations",                         # dropdown
    "prolongued_decelerations",                     # dropdown
    "abnormal_short_term_variability",
    "mean_value_of_short_term_variability",
    "percentage_of_time_with_abnormal_long_term_variability",
    "mean_value_of_long_term_variability",
    "histogram_width",
    "histogram_min",
    "histogram_max",
    "histogram_number_of_peaks",
    "histogram_number_of_zeroes",                   # dropdown
    "histogram_mode",
    "histogram_mean",
    "histogram_median",
    "histogram_variance",
    "histogram_tendency"                            # dropdown
]

# UI layout
st.set_page_config("Fetal Health Prediction Form", layout="wide")
st.title("🤰 Fetal Health Prediction Form")

st.write("Please fill in the following details:")

with st.form("fetal_health_form"):
    cols = st.columns(3)
    user_input = {}

    for i, feature in enumerate(feature_names):
        with cols[i % 3]:
            if feature in categorical_dropdowns:
                user_input[feature] = st.selectbox(f"{feature}", options=categorical_dropdowns[feature], format_func=lambda x: f"{x:.3f}" if isinstance(x, float) else str(x))
            else:
                user_input[feature] = st.number_input(f"{feature}", format="%.5f")

    submitted = st.form_submit_button("Predict Fetal Health")

if submitted:
    try:
        input_array = pd.DataFrame([user_input])
        input_scaled = preprocessor.transform(input_array)
        prediction = model.predict(input_scaled)[0]

        label_map = {
            0: "Normal (Class 1)",
            1: "Suspect (Class 2)",
            2: "Pathological (Class 3)"
        }

        st.subheader("🩺 Prediction Result")
        st.success(f"Predicted fetal health class: **{label_map[prediction]}**")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
