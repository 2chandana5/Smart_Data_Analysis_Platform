import streamlit as st
import pandas as pd


def report_generator(df):

  

    st.write("Generate a quick report of your uploaded dataset.")

    # Convert object columns to string
    report_df = df.copy()

    for col in report_df.select_dtypes(include=["object"]).columns:
        report_df[col] = report_df[col].astype(str)

    # ---------------------------------
    # Dataset Overview
    # ---------------------------------

    st.subheader("📊 Dataset Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Rows", report_df.shape[0])

    with c2:
        st.metric("Columns", report_df.shape[1])

    with c3:
        st.metric("Missing Values", int(report_df.isnull().sum().sum()))

    with c4:
        st.metric("Duplicate Rows", int(report_df.duplicated().sum()))

    # ---------------------------------
    # Data Types
    # ---------------------------------

    st.subheader("🔤 Data Types")

    datatype_df = pd.DataFrame({
        "Column": report_df.columns,
        "Data Type": report_df.dtypes.astype(str)
    })

    st.dataframe(datatype_df, width="stretch")

    # ---------------------------------
    # Summary Statistics
    # ---------------------------------

    st.subheader("📈 Summary Statistics")

    try:
        st.dataframe(
            report_df.describe(include="all"),
            width="stretch"
        )

    except Exception:

        st.warning("Summary statistics not available.")

    # ---------------------------------
    # Download Dataset
    # ---------------------------------

    st.subheader("⬇ Download Dataset")

    csv = report_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="dataset_report.csv",
        mime="text/csv"
    )

    st.success("✅ Report Generated Successfully!")