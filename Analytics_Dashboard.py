import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load sample data
@st.cache_data
def load_data():
    data = pd.DataFrame({
        'Date': pd.date_range(start='2022-01-01', end='2022-12-31'),
        'RandomValue': np.random.randn(365).cumsum()
    })
    return data

data = load_data()

# Sidebar with user inputs
st.sidebar.header('User Inputs')

# Convert DataFrame column to scalar values for min and max
min_date = data['Date'].min().date()
max_date = data['Date'].max().date()

start_date = st.sidebar.date_input('Start Date', min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input('End Date', min_value=min_date, max_value=max_date, value=max_date)
selected_metric = st.sidebar.selectbox('Select Metric', ['RandomValue'])

# Filter data based on user inputs
filtered_data = data[(data['Date'].dt.date >= start_date) & (data['Date'].dt.date <= end_date)]

# Main content
st.title('Big Streamlit Project')

# Display filtered data table
st.subheader('Filtered Data')
st.write(filtered_data)

# Plotly chart
fig = px.line(filtered_data, x='Date', y=selected_metric, title=f'{selected_metric} over time')
st.plotly_chart(fig)

# Additional analysis or machine learning model integration can be added here

# About section
st.sidebar.markdown('---')
st.sidebar.subheader('About')
st.sidebar.write('This is a Streamlit app demonstrating a big Streamlit project.')
