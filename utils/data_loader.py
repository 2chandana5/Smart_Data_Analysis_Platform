import streamlit as st
import pandas as pd

def show_data_loader():

    st.markdown("""
    <style>

    .upload-box{
        background:#111827;
        padding:25px;
        border-radius:15px;
        border:1px solid #1f2937;
        margin-bottom:20px;
    }

    .info-card{
        background:#111827;
        padding:18px;
        border-radius:12px;
        border:1px solid #1f2937;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="upload-box">
        <h2>📂 Upload Your Dataset</h2>
        <p>Upload a CSV or Excel file to begin your analysis.</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose a Dataset",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:

            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)

            else:
                df = pd.read_excel(uploaded_file)

            st.session_state["df"] = df

            st.success("✅ Dataset uploaded successfully!")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("Rows", df.shape[0])

            with c2:
                st.metric("Columns", df.shape[1])

            with c3:
                memory = round(df.memory_usage(deep=True).sum()/1024,2)
                st.metric("Memory (KB)", memory)

            st.markdown("---")

            st.subheader("📋 Dataset Preview")

            st.dataframe(
                df.head(10),
                use_container_width=True,
                height=350
            )

            st.markdown("---")

            st.subheader("📊 Dataset Information")

            col1, col2 = st.columns(2)

            with col1:

                st.write("**Column Names**")

                st.write(list(df.columns))

            with col2:

                st.write("**Data Types**")

                st.dataframe(
                    df.dtypes.astype(str),
                    use_container_width=True
                )

        except Exception as e:

            st.error(f"❌ Error loading dataset: {e}")

    else:

        st.info("Upload a CSV or Excel file to continue.")