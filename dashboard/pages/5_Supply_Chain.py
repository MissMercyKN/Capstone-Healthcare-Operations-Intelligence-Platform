import streamlit as st
import plotly.express as px

from utils.data_loader import load_table


st.title(
    "Supply Chain Analytics"
)


inventory = load_table(
    "inventory"
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