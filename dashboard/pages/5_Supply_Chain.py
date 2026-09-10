import streamlit as st
import plotly.express as px

import pandas as pd


st.title(
    "Supply Chain Analytics"
)


inventory = pd.read_csv(
    "data/deployment/inventory.csv"
)



fig = px.bar(
    inventory,
    x="item_name",
    y="current_stock",
    title="Current Inventory Levels"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



st.dataframe(
    inventory
)