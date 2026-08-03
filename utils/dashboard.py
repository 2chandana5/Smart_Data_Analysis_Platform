import streamlit as st
import pandas as pd

def show_dashboard():

    st.markdown("""
    <style>
    .banner{
        background: linear-gradient(90deg,#0b1f3a,#081018);
        padding:25px;
        border-radius:15px;
        color:white;
        margin-bottom:20px;
    }

    .metric-box{
        background:#111827;
        padding:18px;
        border-radius:12px;
        text-align:center;
        border:1px solid #1f2937;
    }

    .metric-title{
        color:#9CA3AF;
        font-size:15px;
    }

    .metric-value{
        color:white;
        font-size:32px;
        font-weight:bold;
    }

    .section{
        background:#111827;
        padding:20px;
        border-radius:15px;
        margin-top:20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="banner">
        <h4>👋 Welcome Back!</h4>
        <h1>AI Data Analyst Assistant</h1>
        <h4>Analyze • Clean • Visualize • Generate Insights</h4>
        <p>Upload your dataset and let AI uncover powerful insights.</p>
    </div>
    """, unsafe_allow_html=True)

    df = st.session_state.get("df")

    if df is not None:

        rows = df.shape[0]
        cols = df.shape[1]
        missing = df.isnull().sum().sum()
        duplicate = df.duplicated().sum()

    else:

        rows = 0
        cols = 0
        missing = 0
        duplicate = 0

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="metric-box">
        <div class="metric-title">📄 Total Rows</div>
        <div class="metric-value">{rows}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-box">
        <div class="metric-title">📊 Columns</div>
        <div class="metric-value">{cols}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-box">
        <div class="metric-title">❓ Missing Values</div>
        <div class="metric-value">{missing}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="metric-box">
        <div class="metric-title">📋 Duplicates</div>
        <div class="metric-value">{duplicate}</div>
        </div>
        """, unsafe_allow_html=True)

    left,right = st.columns([2,1])

    with left:

        st.markdown("## 📋 Dataset Preview")

        if df is not None:

            st.dataframe(df.head(), use_container_width=True)

        else:

            st.info("Upload a dataset to preview it.")

    with right:

        st.markdown("## 📈 Dataset Overview")

        st.write(f"Rows : **{rows}**")
        st.write(f"Columns : **{cols}**")
        st.write(f"Missing Values : **{missing}**")
        st.write(f"Duplicate Rows : **{duplicate}**")

    st.markdown("---")

    st.markdown("## 🚀 Get Started")

    a,b,c,d = st.columns(4)

    a.success("📂 Upload Dataset")
    b.info("🧹 Clean Data")
    c.warning("📊 Visualize")
    d.success("🤖 AI Insights")