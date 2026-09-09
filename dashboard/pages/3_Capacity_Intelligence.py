import streamlit as st
import plotly.express as px

from utils.data_loader import load_features


st.title(
    "Capacity Intelligence"
)


df = load_features()



capacity = (
    df.groupby("department")
    .agg(
        occupancy=(
            "occupancy_rate",
            "mean"
        )
    )
    .reset_index()
)



fig = px.bar(
    capacity,
    x="department",
    y="occupancy",
    title="Average Occupancy Pressure"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



for _,row in capacity.iterrows():

    if row["occupancy"] >=85:

        st.error(
            f"{row['department']} requires capacity review"
        )

    elif row["occupancy"] >=70:

        st.warning(
            f"{row['department']} under monitoring"
        )

    else:

        st.success(
            f"{row['department']} operating normally"
        )