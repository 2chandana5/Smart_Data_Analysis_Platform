import streamlit as st


def show_ai_assistant(df):

    st.title("🤖 AI Data Assistant")
    st.write("Ask questions about your dataset and receive intelligent insights.")

    # -----------------------------------
    # Dataset Summary
    # -----------------------------------

    rows = df.shape[0]
    cols = df.shape[1]
    missing = int(df.isnull().sum().sum())
    duplicates = int(df.duplicated().sum())

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", rows)
    c2.metric("Columns", cols)
    c3.metric("Missing", missing)
    c4.metric("Duplicates", duplicates)

    st.divider()

    # -----------------------------------
    # Dataset Health
    # -----------------------------------

    st.subheader("📊 Dataset Health")

    if missing == 0 and duplicates == 0:
        st.success("Excellent! Your dataset is clean and ready for analysis.")
    elif missing < rows * 0.05:
        st.info("Good dataset. Only a few missing values detected.")
    else:
        st.warning("Dataset requires cleaning before analysis.")

    st.divider()

    # -----------------------------------
    # Suggested Questions
    # -----------------------------------

    st.subheader("💡 Suggested Questions")

    st.markdown("""
- How many rows are there?
- How many columns are there?
- Are there missing values?
- Are there duplicate rows?
- Show numeric columns.
- Show categorical columns.
- What is the highest value?
- What is the lowest value?
- Show the average values.
""")

    st.divider()

    # -----------------------------------
    # Ask Question
    # -----------------------------------

    question = st.text_input(
        "Ask your question",
        placeholder="Example: How many rows are there?"
    )

    if not question:
        return

    q = question.lower()

    # Dataset Shape

    if "row" in q:

        st.success(f"The dataset contains **{rows}** rows.")

    elif "column" in q:

        st.success(f"The dataset contains **{cols}** columns.")

    # Missing Values

    elif "missing" in q:

        st.success(f"Total missing values: **{missing}**")

    # Duplicate Rows

    elif "duplicate" in q:

        st.success(f"Duplicate rows: **{duplicates}**")

    # Numeric Columns

    elif "numeric" in q:

        st.subheader("Numeric Columns")

        st.write(numeric_cols)

    # Categorical Columns

    elif "categorical" in q:

        st.subheader("Categorical Columns")

        st.write(categorical_cols)

    # Highest Value

    elif "highest" in q or "maximum" in q:

        numeric = df.select_dtypes(include="number")

        if numeric.empty:

            st.warning("No numeric columns available.")

        else:

            column = numeric.max().idxmax()
            value = numeric.max().max()

            st.success(
                f"The highest value is **{value}** in **{column}**."
            )

    # Lowest Value

    elif "lowest" in q or "minimum" in q:

        numeric = df.select_dtypes(include="number")

        if numeric.empty:

            st.warning("No numeric columns available.")

        else:

            column = numeric.min().idxmin()
            value = numeric.min().min()

            st.success(
                f"The lowest value is **{value}** in **{column}**."
            )

    # Mean

    elif "mean" in q or "average" in q:

        st.subheader("Average Values")

        st.dataframe(
            df.mean(numeric_only=True),
            use_container_width=True
        )

    # Dataset Summary

    elif "summary" in q:

        st.write(f"Rows : **{rows}**")
        st.write(f"Columns : **{cols}**")
        st.write(f"Numeric Columns : **{len(numeric_cols)}**")
        st.write(f"Categorical Columns : **{len(categorical_cols)}**")

    # Visualization Suggestion

    elif "visualization" in q or "chart" in q:

        st.info("""
Recommended Charts

• Histogram → Distribution

• Scatter Plot → Relationship

• Bar Chart → Categories

• Pie Chart → Category Share

• Heatmap → Correlation
""")

    # Default

    else:

       st.info("""
🤖 Sorry, I don't have enough information to answer that query.

Try asking one of these:

📊 Summarize my dataset

📈 Show missing values

📋 List numeric columns

🧹 Check duplicate rows

📉 Show average values

💡 Recommend the best charts
""")