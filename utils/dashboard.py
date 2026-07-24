import streamlit as st


def dashboard(df):

    st.title("📊 Dashboard")

    st.markdown("### Welcome to AI Data Analyst Assistant")

    st.write("Analyze, clean, visualize and generate insights from your dataset.")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("📄 Rows", df.shape[0])

    with c2:
        st.metric("📑 Columns", df.shape[1])

    with c3:
        st.metric("❓ Missing", int(df.isnull().sum().sum()))

    with c4:
        st.metric("🗑 Duplicates", int(df.duplicated().sum()))

    st.divider()

    st.subheader("📋 Dataset Preview")

    st.dataframe(df.head(10), width="stretch")

    st.divider()

    st.subheader("🚀 Quick Information")

    col1, col2 = st.columns(2)

    with col1:

        st.success("✔ Dataset Uploaded")

        st.info(f"Numeric Columns : {len(df.select_dtypes(include='number').columns)}")

        st.info(f"Categorical Columns : {len(df.select_dtypes(exclude='number').columns)}")

    with col2:

        st.warning("Ready for Cleaning")

        st.success("Ready for Visualization")

        st.success("Ready for Report Generation")