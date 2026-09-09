import streamlit as st
import plotly.express as px

from utils.data_loader import load_features


st.title(
    "Patient Flow Analytics"
)


df = load_features()


department = st.sidebar.selectbox(
    "Department",
    ["All"] +
    sorted(
        df.department.unique()
    )
)


if department != "All":

    df = df[
        df.department == department
    ]



c1,c2,c3 = st.columns(3)


with c1:
    st.metric(
        "Patient Volume",
        round(
            df.patient_volume.mean()
        )
    )


with c2:
    st.metric(
        "Waiting Time",
        f"{round(df.avg_wait_time.mean(),1)} min"
    )


with c3:
    st.metric(
        "Treatment Time",
        f"{round(df.avg_treatment_time.mean(),1)} min"
    )



fig = px.line(
    df,
    x="date",
    y="patient_volume",
    color="department",
    title="Patient Demand Trend"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



fig2 = px.scatter(
    df,
    x="avg_wait_time",
    y="risk_score",
    color="department",
    title="Waiting Time vs Risk"
)


st.plotly_chart(
    fig2,
    use_container_width=True
)