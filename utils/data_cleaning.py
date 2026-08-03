import streamlit as st
import pandas as pd


def show_data_cleaning():

    st.title("🧹 Data Cleaning")

    if "df" not in st.session_state:

        st.warning("⚠ Please upload a dataset first.")

        return

    df = st.session_state["df"].copy()

    st.subheader("Dataset Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Missing Values", int(df.isnull().sum().sum()))

    st.markdown("---")

    st.subheader("Missing Values")

    missing = df.isnull().sum()

    st.dataframe(
        missing[missing > 0].rename("Missing Count"),
        use_container_width=True
    )

    option = st.selectbox(
        "Handle Missing Values",
        (
            "Do Nothing",
            "Drop Missing Rows",
            "Fill Numeric with Mean",
            "Fill Numeric with Median",
            "Fill Categorical with Mode"
        )
    )

    if st.button("Apply Missing Value Handling"):

        if option == "Drop Missing Rows":

            df = df.dropna()

        elif option == "Fill Numeric with Mean":

            numeric_cols = df.select_dtypes(include="number").columns

            for col in numeric_cols:
                df[col] = df[col].fillna(df[col].mean())

        elif option == "Fill Numeric with Median":

            numeric_cols = df.select_dtypes(include="number").columns

            for col in numeric_cols:
                df[col] = df[col].fillna(df[col].median())

        elif option == "Fill Categorical with Mode":

            cat_cols = df.select_dtypes(exclude="number").columns

            for col in cat_cols:

                if not df[col].mode().empty:
                    df[col] = df[col].fillna(df[col].mode()[0])

        st.session_state["df"] = df

        st.success("✅ Missing values handled successfully!")

    st.markdown("---")

    st.subheader("Duplicate Rows")

    duplicates = int(df.duplicated().sum())

    st.metric("Duplicate Rows", duplicates)

    if st.button("Remove Duplicate Rows"):

        df = df.drop_duplicates()

        st.session_state["df"] = df

        st.success("✅ Duplicate rows removed!")

    st.markdown("---")

    st.subheader("Cleaned Dataset Preview")

    st.dataframe(
        st.session_state["df"].head(10),
        use_container_width=True
    )

    csv = st.session_state["df"].to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Cleaned Dataset",
        csv,
        "cleaned_dataset.csv",
        "text/csv"
    )