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
        margin-top: -60px;  /* Adjust this value to remove white space */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        margin-bottom: 0px;  /* Adjust this value to reduce space */
    }
    .main {
        margin-left: -70px;  /* Adjust this value to reduce space */
        margin-right: 0px;  /* Adjust this value to reduce space */
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
selected_model = st.sidebar.selectbox('Select Model', model_options, key='model')

# Update type options based on selected model
type_options = df[df['Models'] == selected_model]['Type'].unique()
selected_type = st.sidebar.selectbox('Select Type', type_options, key='type')

# Update main group options based on selected model and type
main_group_options = df[(df['Models'] == selected_model) & (df['Type'] == selected_type)]['Main Group'].unique()
selected_main_group = st.sidebar.selectbox('Select Main Group', main_group_options, key='main_group')

# Update new disc options based on selected model, type, and main group
new_disc_options = df[(df['Models'] == selected_model) & (df['Type'] == selected_type) &
                      (df['Main Group'] == selected_main_group)]['New Disc'].unique()
selected_new_disc = st.sidebar.selectbox('Select New Disc', new_disc_options, key='new_disc')


# Filter data based on user selection
filtered_data = df[(df['Models'] == selected_model) &
                   (df['Type'] == selected_type) &
                   (df['Main Group'] == selected_main_group) &
                   (df['New Disc'] == selected_new_disc)]

# Specify columns to be displayed in the table
table_columns = ['Part No', 'Description', 'Location', 'Current Stock', 'MRP']

fig = go.Figure(data=[go.Table(columnwidth = [80,170,70,70,70],
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
        margin-top: -60px;  /* Adjust this value to remove white space */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        margin-bottom: 0px;  /* Adjust this value to reduce space */
    }
    .main {
        margin-left: -70px;  /* Adjust this value to reduce space */
        margin-right: 0px;  /* Adjust this value to reduce space */
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
selected_model = st.sidebar.selectbox('Select Model', model_options, key='model')

# Update type options based on selected model
type_options = df[df['Models'] == selected_model]['Type'].unique()
selected_type = st.sidebar.selectbox('Select Type', type_options, key='type')

# Update main group options based on selected model and type
main_group_options = df[(df['Models'] == selected_model) & (df['Type'] == selected_type)]['Main Group'].unique()
selected_main_group = st.sidebar.selectbox('Select Main Group', main_group_options, key='main_group')

# Update new disc options based on selected model, type, and main group
new_disc_options = df[(df['Models'] == selected_model) & (df['Type'] == selected_type) &
                      (df['Main Group'] == selected_main_group)]['New Disc'].unique()
selected_new_disc = st.sidebar.selectbox('Select New Disc', new_disc_options, key='new_disc')


# Filter data based on user selection
filtered_data = df[(df['Models'] == selected_model) &
                   (df['Type'] == selected_type) &
                   (df['Main Group'] == selected_main_group) &
                   (df['New Disc'] == selected_new_disc)]

# Specify columns to be displayed in the table
table_columns = ['Part No', 'Description', 'Location', 'Current Stock', 'MRP']

fig = go.Figure(data=[go.Table(columnwidth = [80,170,70,70,70],
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
fig.update_layout(width=800, height=300, title=dict(text='Part Details', font=dict(size=20, family='sans-serif')), margin=dict(b=0, l=0, r=0))

# Display Plotly table
st.plotly_chart(fig)


# Select columns 14 to 31
#selected_columns = filtered_data.iloc[:, 14:32]

# Transpose the selected columns
#transposed_data = selected_columns.T

# Display the transposed table using st.write
#st.table(transposed_data)


# Select columns 14 to 31
selected_columns = filtered_data.iloc[:, 14:32]

# Get values from column 6
column_6_values = filtered_data.iloc[:, 5].values

# Transpose selected columns
transposed_data = selected_columns.T

# Set column names as transformed data
transposed_data.columns = column_6_values




# Define CSS classes for table formatting
css_classes = [{'selector': 'table',
                'props': [('border-collapse', 'collapse'),
                          ('border', '1px solid #000'),
                          ('border-color', 'black')]},
               {'selector': 'th:first-child',
                'props': [('font-weight', 'bold'),
                          ('text-align', 'center'),
                          ('color', '#384252'),
                          ('border', '1px solid #000'),
                          ('border-color', 'black')]},
               {'selector': 'th:not(:first-child)',
                'props': [('text-align', 'center'),
                          ('font-weight', 'bold'),
                          ('color', '#2c8cff'),
                          ('border', '1px solid #000'),
                          ('border-color', 'black')]},
               {'selector': 'td',
                'props': [('text-align', 'center'),
                          ('margin-left', 'auto'),
                          ('margin-right', 'auto'),
                          ('border', '1px solid #000'),
                          ('border-color', 'black')]},  # Set the border color to black
               {'selector': '.dataframe',  # Add margin reduction styles
                'props': [('margin-top', '-100px'),
                          ('margin-bottom', '-50px')]},  # Set negative margins to reduce spacing
               {'selector': '.dataframe th, .dataframe td',  # Add padding reduction styles
                'props': [('padding-top', '-100px'),
                          ('padding-bottom', '5px'),
                          ('padding-left', '5px'),
                          ('padding-right', '5px')]  # Set padding values to reduce spacing
                }]




# Apply formatting to the dataframe
formatted_df = transposed_data.style.set_table_attributes('class="dataframe"').set_table_styles(css_classes)

# Display the formatted dataframe using st.write() with html string

st.write(formatted_df.render(), unsafe_allow_html=True)

# Apply formatting to the dataframe
#formatted_df = transposed_data.style.set_table_attributes('class="dataframe"').set_table_styles(css_classes)

# Display the formatted dataframe using st.table
#st.table(formatted_df)
