import streamlit as st
import plotly.express as px


def show_visualization(df):

    st.title("📊 Data Visualization")
    st.write("Explore your dataset using interactive charts.")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(exclude="number").columns.tolist()

    # -----------------------------
    # Dataset Summary
    # -----------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Numeric", len(numeric_columns))
    c4.metric("Categorical", len(categorical_columns))

    st.divider()

    # -----------------------------
    # Chart Selection
    # -----------------------------

    left, right = st.columns(2)

    with left:

        chart = st.selectbox(
            "📈 Select Chart",
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

        with right:
            column = st.selectbox(
                "Select Numeric Column",
                numeric_columns
            )

        fig = px.histogram(
            df,
            x=column,
            title=f"Distribution of {column}"
        )

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            f"""
**Insights**

• Total Records : {len(df)}

• Missing Values : {df[column].isnull().sum()}

• Mean : {round(df[column].mean(),2)}
"""
        )

    # -----------------------------
    # Scatter Plot
    # -----------------------------

    elif chart == "Scatter Plot":

        if len(numeric_columns) < 2:
            st.warning("Need at least two numeric columns.")
            return

        with right:

            x = st.selectbox("X Axis", numeric_columns)

            y = st.selectbox(
                "Y Axis",
                numeric_columns,
                index=1
            )

        fig = px.scatter(
            df,
            x=x,
            y=y,
            title=f"{x} vs {y}"
        )

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            f"""
**Insights**

• X Axis : {x}

• Y Axis : {y}

• Records : {len(df)}
"""
        )

    # -----------------------------
    # Box Plot
    # -----------------------------

    elif chart == "Box Plot":

        if not numeric_columns:
            st.warning("No numeric columns available.")
            return

        with right:
            column = st.selectbox(
                "Select Numeric Column",
                numeric_columns
            )

        fig = px.box(
            df,
            y=column,
            title=f"Box Plot of {column}"
        )

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            f"""
**Insights**

• Median : {round(df[column].median(),2)}

• Maximum : {df[column].max()}

• Minimum : {df[column].min()}
"""
        )

    # -----------------------------
    # Line Chart
    # -----------------------------

    elif chart == "Line Chart":

        if not numeric_columns:
            st.warning("No numeric columns available.")
            return

        with right:
            column = st.selectbox(
                "Select Numeric Column",
                numeric_columns
            )

        fig = px.line(
            df,
            y=column,
            title=f"Trend of {column}"
        )

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # Bar Chart
    # -----------------------------

    elif chart == "Bar Chart":

        if not categorical_columns:
            st.warning("No categorical columns available.")
            return

        with right:
            column = st.selectbox(
                "Select Categorical Column",
                categorical_columns
            )

        value_counts = df[column].value_counts().reset_index()
        value_counts.columns = [column, "Count"]

        fig = px.bar(
            value_counts,
            x=column,
            y="Count",
            title=f"{column} Distribution"
        )

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, use_container_width=True)

        st.info(
            f"""
**Insights**

• Categories : {df[column].nunique()}

• Most Frequent : {df[column].mode()[0]}
"""
        )

    # -----------------------------
    # Pie Chart
    # -----------------------------

    elif chart == "Pie Chart":

        if not categorical_columns:
            st.warning("No categorical columns available.")
            return

        with right:
            column = st.selectbox(
                "Select Categorical Column",
                categorical_columns
            )

        value_counts = df[column].value_counts().reset_index()
        value_counts.columns = [column, "Count"]

        fig = px.pie(
            value_counts,
            names=column,
            values="Count",
            title=f"{column} Distribution"
        )

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, use_container_width=True)

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
            color_continuous_scale="RdBu",
            title="Correlation Heatmap"
        )

        fig.update_layout(template="plotly_dark")

        st.plotly_chart(fig, use_container_width=True)

        st.success("Correlation matrix generated successfully.")