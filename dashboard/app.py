import streamlit as st


st.set_page_config(
    page_title="Healthcare Operations Intelligence Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Custom styling

st.markdown(
    """
    <style>

    .main {
        background-color: #0F172A;
    }


    h1, h2, h3 {
        color: #F8FAFC;
    }


    p, label {
        color: #CBD5E1;
    }


    .stMetric {

        background-color: #1E293B;

        padding: 20px;

        border-radius: 12px;

    }


    div[data-testid="stSidebar"] {

        background-color: #111827;

    }


    </style>

    """,
    unsafe_allow_html=True
)



st.title(
    "🏥 Healthcare Operations Intelligence Platform"
)


st.subheader(
    "Executive Decision Support Command Center"
)


st.markdown(
    """
    This platform integrates:

    - Healthcare operational data

    - Capacity and workforce intelligence

    - Predictive machine learning models

    - Executive decision support analytics

    """
)