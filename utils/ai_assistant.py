import streamlit as st


def ai_assistant(df):

   

    st.write("Ask questions about your uploaded dataset.")

    question = st.text_input(
        "Ask a question",
        placeholder="Example: How many rows are there?"
    )

    if not question:
        return

    q = question.lower()

    # ------------------------------------
    # Dataset Shape
    # ------------------------------------

    if "row" in q:

        st.success(f"The dataset contains {df.shape[0]} rows.")

    elif "column" in q:

        st.success(f"The dataset contains {df.shape[1]} columns.")

    # ------------------------------------
    # Missing Values
    # ------------------------------------

    elif "missing" in q:

        st.success(
            f"Total missing values: {df.isnull().sum().sum()}"
        )

    # ------------------------------------
    # Duplicates
    # ------------------------------------

    elif "duplicate" in q:

        st.success(
            f"Duplicate rows: {df.duplicated().sum()}"
        )

    # ------------------------------------
    # Numeric Columns
    # ------------------------------------

    elif "numeric" in q:

        cols = df.select_dtypes(include="number").columns.tolist()

        st.write(cols)

    # ------------------------------------
    # Categorical Columns
    # ------------------------------------

    elif "categorical" in q:

        cols = df.select_dtypes(exclude="number").columns.tolist()

        st.write(cols)

    # ------------------------------------
    # Highest Value
    # ------------------------------------

    elif "highest" in q or "maximum" in q:

        numeric = df.select_dtypes(include="number")

        if numeric.empty:

            st.warning("No numeric columns available.")

        else:

            column = numeric.max().idxmax()

            value = numeric.max().max()

            st.success(
                f"Highest value is {value} in '{column}'."
            )

    # ------------------------------------
    # Lowest Value
    # ------------------------------------

    elif "lowest" in q or "minimum" in q:

        numeric = df.select_dtypes(include="number")

        if numeric.empty:

            st.warning("No numeric columns available.")

        else:

            column = numeric.min().idxmin()

            value = numeric.min().min()

            st.success(
                f"Lowest value is {value} in '{column}'."
            )

    # ------------------------------------
    # Mean
    # ------------------------------------

    elif "mean" in q or "average" in q:

        st.dataframe(df.mean(numeric_only=True))

    # ------------------------------------
    # Default
    # ------------------------------------

    else:

        st.info(
            "I can answer questions about rows, columns, missing values, duplicates, highest, lowest, mean, numeric columns and categorical columns."
        )