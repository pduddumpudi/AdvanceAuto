import functools
from pathlib import Path

import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
import plotly.express as px

import streamlit as st
import pandas as pd

# Load Excel file
df = pd.read_excel('Input.xlsx')

# Define sidebar location
st.sidebar.markdown('<h1 style="color:#2c8cff; font-weight: bold;">Advance Auto Parts</h1>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="color:#384252; font-weight: bold; font-size:16px;">Welcome to the CBS Dashboard</p>', unsafe_allow_html=True)

# Create dropdowns for user selection
model_options = df['Models'].unique()
selected_model = st.sidebar.selectbox('Select Model', model_options)

# Update type options based on selected model
type_options = df[df['Models'] == selected_model]['Type'].unique()
selected_type = st.sidebar.selectbox('Select Type', type_options)

# Update main group options based on selected model and type
main_group_options = df[(df['Models'] == selected_model) & (df['Type'] == selected_type)]['Main Group'].unique()
selected_main_group = st.sidebar.selectbox('Select Main Group', main_group_options)

# Update new disc options based on selected model, type, and main group
new_disc_options = df[(df['Models'] == selected_model) & (df['Type'] == selected_type) &
                      (df['Main Group'] == selected_main_group)]['New Disc'].unique()
selected_new_disc = st.sidebar.selectbox('Select New Disc', new_disc_options)

# Filter data based on user selection
filtered_data = df[(df['Models'] == selected_model) &
                   (df['Type'] == selected_type) &
                   (df['Main Group'] == selected_main_group) &
                   (df['New Disc'] == selected_new_disc)]

# Display filtered data in a table
st.write(filtered_data[['Part No', 'Description', 'Location', 'Current Stock', 'MRP']])
