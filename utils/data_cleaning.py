import streamlit as st
import pandas as pd


def data_cleaning(df):

   

    clean_df = df.copy()

    # Convert object columns to string
    for col in clean_df.select_dtypes(include=["object"]).columns:
        clean_df[col] = clean_df[col].astype(str)
    # -----------------------------------
    # Remove Duplicate Rows
    # -----------------------------------
    st.subheader("🗑 Remove Duplicate Rows")

    duplicates = clean_df.duplicated().sum()

    st.write(f"Duplicate Rows : **{duplicates}**")

    if st.button("Remove Duplicates"):

        clean_df = clean_df.drop_duplicates()

        st.success("✅ Duplicate rows removed successfully!")

        st.dataframe(clean_df, use_container_width="stretch")

    # -----------------------------------
    # Handle Missing Values
    # -----------------------------------
    st.subheader("❓ Handle Missing Values")

    option = st.selectbox(
        "Choose an option",
        (
            "Do Nothing",
            "Fill Missing Values",
            "Remove Missing Values"
        )
    )

    if option == "Fill Missing Values":

        for col in clean_df.columns:

            if pd.api.types.is_numeric_dtype(clean_df[col]):

                clean_df[col] = clean_df[col].fillna(
                    clean_df[col].mean()
                )

            else:

                mode = clean_df[col].mode()

                if not mode.empty:
                    clean_df[col] = clean_df[col].fillna(mode[0])

        st.success("✅ Missing values filled successfully!")

        st.dataframe(clean_df, use_container_width="stretch")

    elif option == "Remove Missing Values":

        clean_df = clean_df.dropna()

        st.success("✅ Missing value rows removed!")

        st.dataframe(clean_df, use_container_width="stretch")

    # -----------------------------------
    # Filter Dataset
    # -----------------------------------
    st.subheader("🔍 Filter Dataset")

    filter_column = st.selectbox(
        "Select Column",
        clean_df.columns,
        key="filter"
    )

    values = clean_df[filter_column].dropna().unique()

    filter_value = st.selectbox(
        "Select Value",
        values,
        key="value"
    )

    filtered_df = clean_df[
        clean_df[filter_column] == filter_value
    ]

    st.dataframe(filtered_df, use_container_width=True)

    # -----------------------------------
    # Search Dataset
    # -----------------------------------
    st.subheader("🔎 Search Dataset")

    search = st.text_input("Search Anything")

    if search:

        result = clean_df[
            clean_df.astype(str)
            .apply(
                lambda x: x.str.contains(
                    search,
                    case=False,
                    na=False
                )
            )
            .any(axis=1)
        ]

        st.dataframe(result, use_container_width=True)

    # -----------------------------------
    # Download Cleaned Dataset
    # -----------------------------------
    st.subheader("⬇ Download Cleaned Dataset")

    csv = clean_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download CSV",
        csv,
        "cleaned_dataset.csv",
        "text/csv"
    )

    return clean_df