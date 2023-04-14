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

# Define custom CSS for the sidebar
sidebar_style = """
    .sidebar {
        margin-left: 0px;
    }
"""

# Apply custom CSS
st.markdown('<style>{}</style>'.format(sidebar_style), unsafe_allow_html=True)

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

# Display table title
st.markdown('<h2 style="font-size: 20px; font-weight: bold;">Part Details</h2>', unsafe_allow_html=True)

# Display filtered data using AgGrid
gb = GridOptionsBuilder.from_dataframe(filtered_data)
grid_options = gb.build()

AgGrid(filtered_data, gridOptions=grid_options, width=3000, height=500)

# Set custom formatting for the columns
grid_options = {
    'columnDefs': [
        {'field': 'Part No', 'headerName': 'Part No', 'width': 250, 'headerClass': 'ag-header-bold'},
        {'field': 'Description', 'headerName': 'Description', 'width': 250, 'headerClass': 'ag-header-bold'},
        {'field': 'Location', 'headerName': 'Location', 'width': 250, 'headerClass': 'ag-header-bold'},
        {'field': 'Current Stock', 'headerName': 'Current Stock', 'width': 250, 'headerClass': 'ag-header-bold'},
        {'field': 'MRP', 'headerName': 'MRP', 'width': 250, 'headerClass': 'ag-header-bold'}
    ],
    'rowData': filtered_data.to_dict('records'),
    'fitColumns': True,
    'rowSelection': 'multiple',  # or 'single',
       'useCheckboxSelection': True,  # Enable checkbox selection
    'checkboxSelectionMode': 'single',  # or 'multiple' for multiple selection
    'maxHeight': 300,  # Maximum height of the table
    'defaultColDef': {  # Default column definition
        'sortable': True,  # Enable sorting
        'resizable': True,  # Enable column resizing
        'suppressMenu': True,  # Disable column menu
        'floatingFilter': True,  # Enable floating filters
    },
    'suppressRowClickSelection': True,  # Disable row selection by clicking on the row
    'enableFilter': True,  # Enable global filters
    'pagination': True,  # Enable pagination
    'paginationPageSize': 20,  # Number of rows per page
    'overlayNoRowsTemplate': '<span style="padding: 10px;">No data available</span>',  # Template for empty table
}

# Render AgGrid table
grid_response = AgGrid(filtered_data, gridOptions=grid_options, width='100%', height='300px')

# Get selected rows
selected_rows = grid_response['selected_rows']

# Display selected rows data
if selected_rows:
    st.markdown('<h3 style="font-size: 18px; font-weight: bold;">Selected Part Details</h3>', unsafe_allow_html=True)
    selected_data = filtered_data.iloc[selected_rows]
    st.write(selected_data)
