import functools
from pathlib import Path

import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import streamlit as st
import pandas as pd

from st_aggrid import AgGrid, GridOptionsBuilder


# Load Excel file
df = pd.read_excel('Input.xlsx')
# Add CSS to remove white space at the top
st.markdown(
    """
    <style>
    .stApp {
        margin-top: -100px;  /* Adjust this value to remove white space */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Apply custom CSS
#st.markdown('<style>{}</style>'.format(sidebar_style), unsafe_allow_html=True)

# Define sidebar location
st.sidebar.markdown('<h1 style="color:#2c8cff; font-weight: bold;">Advance Auto Parts</h1>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="color:#384252; font-weight: bold; font-size:32px;">Welcome to the CBS Dashboard</p>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="color:#384252;font-size:14px;">Explore auto parts location and availability. Select the below filters to view</p>', unsafe_allow_html=True)

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

# Specify columns to be displayed in the table
table_columns = ['Part No', 'Description', 'Location', 'Current Stock', 'MRP']

fig = go.Figure(data=[go.Table(columnwidth = [80,170,70,70,50],
    header=dict(values= ['<b>' + entry + '</b>' for entry in table_columns],
                fill_color='white',
                line_color='darkslategray',
                align='center',
                font=dict(color='#2c8cff', size=14, family='sans-serif')),
    cells=dict(values=[filtered_data[col] for col in table_columns],
               fill_color='white',
               line_color='darkslategray',
               align='center',
               font=dict(color='darkslategray', size=16, family='sans-serif'),
               height=30)
)])

# Update table layout
fig.update_layout(width=800, height=300, title=dict(text='Part Details', font=dict(size=20, family='sans-serif')))

# Display Plotly table
st.plotly_chart(fig)
