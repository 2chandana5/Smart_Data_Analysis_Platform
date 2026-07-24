import streamlit as st
import pandas as pd


def load_data():



    uploaded_file = st.file_uploader(
        "Choose a CSV or Excel file",
        type=["csv", "xlsx"]
    )

    if uploaded_file is None:
        return None

    # ----------------------------
    # Read Dataset
    # ----------------------------
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Convert object columns to string
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str)

  

    # ----------------------------
    # Dataset Preview
    # ----------------------------
    st.subheader("📄 Dataset Preview")
    st.dataframe(df, width="stretch")

    # ----------------------------
    # Dataset Shape
    # ----------------------------
    st.subheader("📏 Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    # ----------------------------
    # Column Names
    # ----------------------------
    st.subheader("📋 Column Names")
    st.write(df.columns.tolist())

    # ----------------------------
    # Data Types
    # ----------------------------
    st.subheader("🔤 Data Types")

    datatype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(datatype_df, width="stretch")

    # ----------------------------
    # Missing Values
    # ----------------------------
    st.subheader("❓ Missing Values")

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values
    })

    st.dataframe(missing_df, width="stretch")

    # ----------------------------
    # Summary Statistics
    # ----------------------------
    st.subheader("📊 Summary Statistics")
    st.dataframe(df.describe(include="all"), width="stretch")

    # ----------------------------
    # First 5 Rows
    # ----------------------------
    st.subheader("🔝 First 5 Rows")
    st.dataframe(df.head(), width="stretch")

    # ----------------------------
    # Last 5 Rows
    # ----------------------------
    st.subheader("🔚 Last 5 Rows")
    st.dataframe(df.tail(), width="stretch")

    # ----------------------------
    # Dataset Information
    # ----------------------------
    st.subheader("ℹ️ Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Rows", df.shape[0])

    with col2:
        st.metric("Total Columns", df.shape[1])

    with col3:
        st.metric("Total Cells", df.size)

    memory = df.memory_usage(deep=True).sum() / 1024
    st.info(f"💾 Memory Usage: {memory:.2f} KB")

    # ----------------------------
    # Dataset Insights
    # ----------------------------
    st.subheader("📌 Dataset Insights")

    numeric_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(exclude="number").columns

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Numeric Columns", len(numeric_cols))

    with c2:
        st.metric("Categorical Columns", len(categorical_cols))

    with c3:
        st.metric("Total Missing Values", int(df.isnull().sum().sum()))

    return df