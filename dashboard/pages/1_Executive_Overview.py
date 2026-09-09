import streamlit as st
import plotly.express as px
import pandas as pd

from utils.data_loader import load_features


st.title(
    "Healthcare Operations Intelligence Platform"
)

st.subheader(
    "Executive Operations Command Center"
)

st.info(
"""
Operational monitoring dashboard.

Current intelligence areas:

🏥 Patient demand

🛏 Capacity pressure

👥 Workforce availability

⚠ Congestion prediction
"""
)

df = load_features()


# KPI calculations

avg_risk = round(
    df["risk_score"].mean(),
    1
)


high_risk_rate = round(
    df["congestion_flag"]
    .mean()
    *100,
    1
)


avg_wait = round(
    df["avg_wait_time"].mean(),
    1
)


avg_occupancy = round(
    df["occupancy_rate"].mean(),
    1
)



# KPI cards

c1,c2,c3,c4 = st.columns(4)


with c1:

    st.metric(
        "⚠ Operational Risk",
        f"{avg_risk}/100"
    )


with c2:

    st.metric(
        "🚨 High Risk Rate",
        f"{high_risk_rate}%"
    )


with c3:

    st.metric(
        "⏱ Waiting Time",
        f"{avg_wait} min"
    )


with c4:

    st.metric(
        "🛏 Occupancy",
        f"{avg_occupancy}%"
    )


st.divider()


# Risk by department

department_risk = (
    df.groupby("department")
    .agg(
        risk_score=(
            "risk_score",
            "mean"
        )
    )
    .reset_index()
)


fig1 = px.bar(
    department_risk,
    x="department",
    y="risk_score",
    title="Operational Risk by Department"
)


st.plotly_chart(
    fig1,
    use_container_width=True
)



# Risk trend

df["date"] = pd.to_datetime(
    df["date"]
)


daily_risk = (
    df.groupby("date")
    ["risk_score"]
    .mean()
    .reset_index()
)


fig2 = px.line(
    daily_risk,
    x="date",
    y="risk_score",
    title="Operational Risk Trend"
)


st.plotly_chart(
    fig2,
    use_container_width=True
)



# Recommendations

st.subheader(
    "Executive Recommendations"
)


highest = (
    department_risk
    .sort_values(
        "risk_score",
        ascending=False
    )
    .iloc[0]
)


st.info(
    f"""
Priority department:

{highest['department']}


Recommended actions:

• Review staffing allocation

• Monitor capacity pressure

• Evaluate patient flow constraints
"""
)