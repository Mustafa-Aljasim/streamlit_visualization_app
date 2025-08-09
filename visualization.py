import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.header("Hello, This is a data visualization app")
st.write("This is a simple Streamlit app running in a virtual environment.")

file = st.file_uploader("Upload a CSV file for visualization", type=["csv"])

@st.cache_data
def load_data(file):
    # Placeholder for loading data
    return pd.read_csv(file)

if file is not None:
    data = load_data(file)

    n_rows = st.slider("Select number of rows to display", 1, len(data), 5)
    showColumn = st.multiselect("Select columns to display", options=data.columns.tolist(), default=data.columns.tolist())
    ##numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    numerical_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    st.write(data[:n_rows][showColumn])

    tab1, tab2 = st.tabs(["Scatter Plot", "Histogram"])
    with tab1:
        col1, col2, col3 = st.columns(3)
        with col1:
            x_axis = st.selectbox("Select X-axis column", options=numerical_columns)
        with col2:
            y_axis = st.selectbox("Select Y-axis column", options=numerical_columns)
        with col3:
            colors = st.selectbox("Select columns for color coding", numerical_columns)
        figure = px.scatter(data, x_axis, y_axis, title="Scatter Plot", color=colors if colors else None)
        st.plotly_chart(figure)
        
    with tab2:
        x_axis = st.selectbox("Select X-axis column for Histogram", options=numerical_columns)
        Hist_fig=px.histogram(data, x=x_axis, title="Histogram", color=colors if colors else None)
        st.plotly_chart(Hist_fig)
        



