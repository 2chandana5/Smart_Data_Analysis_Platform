import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="AI Data Analyst Assistant")

# Title
st.title("🤖 AI Data Analyst Assistant")
st.success("Setup Successful!")
st.write("Welcome to the AI Data Analyst Assistant")

# File Upload
uploaded_file = st.file_uploader(
    "Upload your CSV or Excel file",
    type=["csv", "xlsx"]
)

# Read File
if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("✅ Dataset Uploaded Successfully!")

    # Preview
    st.subheader("Dataset Preview")
    st.dataframe(df)

    # Dataset Information
    st.subheader("Dataset Information")
    st.write("Number of Rows:", df.shape[0])
    st.write("Number of Columns:", df.shape[1])

    # Column Names
    st.subheader("Column Names")
    st.write(df.columns.tolist())

    # Summary Statistics
    st.subheader("Summary Statistics")
    st.dataframe(df.describe(include="all"))