import streamlit as st
import plotly.express as px


def visualization(df):


    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(exclude="number").columns.tolist()

    chart = st.selectbox(
        "Select Chart",
        [
            "Histogram",
            "Scatter Plot",
            "Box Plot",
            "Line Chart",
            "Bar Chart",
            "Pie Chart",
            "Correlation Heatmap"
        ]
    )

    # -----------------------------
    # Histogram
    # -----------------------------
    if chart == "Histogram":

        if not numeric_columns:
            st.warning("No numeric columns available.")
            return

        column = st.selectbox("Select Numeric Column", numeric_columns)

        fig = px.histogram(df, x=column, title=f"Histogram of {column}")

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, width="stretch")

    # -----------------------------
    # Scatter Plot
    # -----------------------------
    elif chart == "Scatter Plot":

        if len(numeric_columns) < 2:
            st.warning("Need at least two numeric columns.")
            return

        x = st.selectbox("X Axis", numeric_columns)

        y = st.selectbox(
            "Y Axis",
            numeric_columns,
            index=1
        )

        fig = px.scatter(df, x=x, y=y, title=f"{x} vs {y}")

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, width="stretch")

    # -----------------------------
    # Box Plot
    # -----------------------------
    elif chart == "Box Plot":

        if not numeric_columns:
            st.warning("No numeric columns available.")
            return

        column = st.selectbox("Select Numeric Column", numeric_columns)

        fig = px.box(df, y=column, title=f"Box Plot of {column}")

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, width="stretch")

    # -----------------------------
    # Line Chart
    # -----------------------------
    elif chart == "Line Chart":

        if not numeric_columns:
            st.warning("No numeric columns available.")
            return

        column = st.selectbox("Select Numeric Column", numeric_columns)

        fig = px.line(df, y=column, title=f"Line Chart of {column}")

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, width="stretch")

    # -----------------------------
    # Bar Chart
    # -----------------------------
    elif chart == "Bar Chart":

        if not categorical_columns:
            st.warning("No categorical columns available.")
            return

        column = st.selectbox("Select Categorical Column", categorical_columns)

        value_counts = df[column].value_counts().reset_index()
        value_counts.columns = [column, "Count"]

        fig = px.bar(
            value_counts,
            x=column,
            y="Count",
            title=f"Bar Chart of {column}"
        )

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, width="stretch")

    # -----------------------------
    # Pie Chart
    # -----------------------------
    elif chart == "Pie Chart":

        if not categorical_columns:
            st.warning("No categorical columns available.")
            return

        column = st.selectbox("Select Categorical Column", categorical_columns)

        value_counts = df[column].value_counts().reset_index()
        value_counts.columns = [column, "Count"]

        fig = px.pie(
            value_counts,
            names=column,
            values="Count",
            title=f"Pie Chart of {column}"
        )

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, width="stretch")

    # -----------------------------
    # Correlation Heatmap
    # -----------------------------
    elif chart == "Correlation Heatmap":

        if len(numeric_columns) < 2:
            st.warning("Need at least two numeric columns.")
            return

        corr = df[numeric_columns].corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            title="Correlation Heatmap",
            color_continuous_scale="Viridis"
        )

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, width="stretch")