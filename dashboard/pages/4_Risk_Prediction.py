import streamlit as st
import pandas as pd
import joblib

from pathlib import Path
from utils.model_loader import load_model


st.title(
    "Operational Risk Prediction"
)


st.write(
    """
    Predict the probability of operational congestion
    using the trained machine learning model.
    """
)


# Load model

MODEL_PATH = Path(
    "models/congestion_prediction_model.pkl"
)


if not MODEL_PATH.exists():

    st.error(
        "Prediction model not found."
    )

    st.stop()



model = joblib.load(
    MODEL_PATH
)


# Input section

st.sidebar.header(
    "Operational Inputs"
)


patient_volume = st.sidebar.number_input(
    "Expected Patient Volume",
    min_value=0,
    value=150
)


avg_wait_time = st.sidebar.number_input(
    "Average Waiting Time (minutes)",
    min_value=0,
    value=60
)


avg_treatment_time = st.sidebar.number_input(
    "Average Treatment Time (minutes)",
    min_value=0,
    value=90
)


occupancy_rate = st.sidebar.slider(
    "Occupancy Rate (%)",
    0,
    100,
    80
)


staff_available = st.sidebar.number_input(
    "Available Staff",
    min_value=1,
    value=20
)


staff_ratio = (
    patient_volume
    /
    staff_available
)


risk_score = st.sidebar.slider(
    "Operational Risk Score",
    0,
    100,
    60
)



# Prediction button

if st.button(
    "Predict Operational Risk"
):

    input_data = pd.DataFrame({

        "patient_volume": [
            patient_volume
        ],

        "avg_wait_time": [
            avg_wait_time
        ],

        "avg_treatment_time": [
            avg_treatment_time
        ],

        "occupancy_rate": [
            occupancy_rate
        ],

        "staff_available": [
            staff_available
        ],

        "staff_ratio": [
            staff_ratio
        ],

        "risk_score": [
            risk_score
        ]

    })


    prediction = model.predict(
        input_data
    )


    probability = model.predict_proba(
        input_data
    )[0][1]


    st.subheader(
        "Prediction Result"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Congestion Probability",
            f"{probability*100:.1f}%"
        )


    with col2:

        if prediction[0] == 1:

            st.error(
                "HIGH OPERATIONAL RISK"
            )

        else:

            st.success(
                "NORMAL OPERATION"
            )


    st.subheader(
        "Operational Interpretation"
    )


    if prediction[0] == 1:

        st.write(
            """
            The model identifies conditions
            associated with increased operational
            congestion risk.

            Recommended actions:

            - Review staffing allocation
            - Monitor waiting times
            - Assess available capacity
            """
        )

    else:

        st.write(
            """
            Current operational conditions
            appear within acceptable limits.
            """
        )