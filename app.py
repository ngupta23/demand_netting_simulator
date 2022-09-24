import pandas as pd
import streamlit as st
from netting_sim import return_netting_outputs

st.title("Demand Netting Simulator")


# Step 1: Get the Inputs
col1, col2, col3 = st.columns(3)
with col1:
    forecast = st.number_input("Forecast", min_value=0)
with col2:
    order = st.number_input("Order", min_value=0)
with col3:
    rtf = st.number_input("RTF", min_value=0)

# Step 2: Plot Netting Results
col1, col2 = st.columns(2)
com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
    forecast=forecast, order=order, rtf=rtf
)

with col1:
    input_chart_data = pd.DataFrame(
        {"Inputs": [forecast, order, rtf]},
        index=["FORECAST", "ORDER", "RTF"],
    )
    st.bar_chart(input_chart_data)

with col2:
    output_chart_data = pd.DataFrame(
        {"Outputs": [com_order, new_order, com_fcst, new_fcst, unf_order]},
        index=["COM_ORDER", "NEW_ORDER", "COM_FCST", "NEW_FCST", "UNF_ORDER"],
    )
    st.bar_chart(output_chart_data)
