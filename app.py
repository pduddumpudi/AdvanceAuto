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

# Create dropdowns for user selection
model_options = df['Models'].unique()
selected_model = st.selectbox('Select Model', model_options)

type_options = df['Type'].unique()
selected_type = st.selectbox('Select Type', type_options)

main_group_options = df['Main Group'].unique()
selected_main_group = st.selectbox('Select Main Group', main_group_options)

new_disc_options = df['New Disc'].unique()
selected_new_disc = st.selectbox('Select New Disc', new_disc_options)

# Filter data based on user selection
filtered_data = df[(df['Models'] == selected_model) &
                   (df['Type'] == selected_type) &
                   (df['Main Group'] == selected_main_group) &
                   (df['New Disc'] == selected_new_disc)]

# Display filtered data in a table
st.write(filtered_data[['Part No', 'Description', 'Location', 'Current Stock', 'MRP']])

