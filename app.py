import streamlit as st

from utils.data_loader import load_data
from utils.data_cleaning import data_cleaning
from utils.visualization import visualization
from utils.ai_assistant import ai_assistant
from utils.report_generator import report_generator
from utils.dashboard import dashboard

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Data Analyst Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM DARK THEME
# ============================================================

st.markdown("""
<style>

/* =========================
   MAIN APP
========================= */

.stApp{
    background:#050816;
    color:white;
}

/* Main Container */

.block-container{
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* =========================
   SIDEBAR
========================= */

[data-testid="stSidebar"]{
    background:#020617;
    border-right:1px solid #1E293B;
}

[data-testid="stSidebar"] *{
    color:white;
}

/* Sidebar Buttons */

.stButton>button{
    background:#16A34A;
    color:white;
    border:none;
    border-radius:12px;
    font-weight:bold;
    width:100%;
    transition:0.3s;
}

.stButton>button:hover{
    background:#22C55E;
}

/* =========================
   HERO SECTION
========================= */

.hero{

background:linear-gradient(
135deg,
#0F172A,
#1E3A8A,
#2563EB
);

padding:40px;

border-radius:20px;

border:1px solid #2563EB;

margin-bottom:30px;

box-shadow:0px 0px 25px rgba(37,99,235,.25);

}

.hero h1{

font-size:44px;

font-weight:700;

color:white;

margin-bottom:10px;

}

.hero h3{

color:#BBF7D0;

font-weight:500;

}

.hero p{

font-size:18px;

color:#CBD5E1;

}

/* =========================
   METRIC CARDS
========================= */

[data-testid="metric-container"]{

background:#111827;

border:1px solid #1F2937;

padding:20px;

border-radius:18px;

box-shadow:0px 0px 10px rgba(0,255,128,.08);

}

/* =========================
   FILE UPLOADER
========================= */

[data-testid="stFileUploader"]{

background:#111827;

border:2px dashed #22C55E;

border-radius:15px;

padding:20px;

}

/* =========================
   DATAFRAME
========================= */

[data-testid="stDataFrame"]{

border-radius:15px;

}

/* =========================
   ALERTS
========================= */

.stSuccess{

background:#064E3B;

color:white;

}

.stWarning{

background:#78350F;

color:white;

}

.stInfo{

background:#1E3A8A;

color:white;

}

/* =========================
   FOOTER
========================= */

.footer{

text-align:center;

padding:15px;

color:#94A3B8;

font-size:15px;

}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HERO
# ============================================================

st.markdown("""

<div class="hero">

<h3>👋 Welcome Back!</h3>

<h1>🤖 AI Data Analyst Assistant</h1>

<p>

Analyze • Clean • Visualize • Generate Reports • AI Insights

</p>

<p>

Upload your dataset and uncover valuable insights using a modern AI-powered analytics platform.

</p>

</div>

""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🤖 AI Data Analyst")

st.sidebar.markdown("### Professional Analytics Suite")

menu = st.sidebar.selectbox(

"Navigation",

[
"🏠 Dashboard",
"📂 Upload Dataset",
"🧹 Data Cleaning",
"📊 Visualization",
"🤖 AI Assistant",
"📄 Report Generator"

]

)

st.sidebar.markdown("---")

st.sidebar.success("🟢 System Ready")

st.sidebar.info("Version 1.0")

# ============================================================
# DASHBOARD
# ============================================================

if menu == "🏠 Dashboard":

    if "df" in st.session_state:

        dashboard(st.session_state["df"])

    else:

        st.title("📊 Dashboard")

        st.info("📂 Upload a dataset to begin your analysis journey.")
 
# ============================================================
# UPLOAD DATASET
# ============================================================

elif menu == "📂 Upload Dataset":

    st.header("📂 Upload Dataset")

    st.write(
        "Upload a CSV or Excel dataset to begin your analysis."
    )

    with st.spinner("Loading Dataset..."):

        df = load_data()

    if df is not None:

        st.session_state["df"] = df

        st.success(
            "✅ Dataset successfully loaded and ready for analysis."
        )

        st.divider()

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "📄 Rows",
                df.shape[0]
            )

        with c2:

            st.metric(
                "📑 Columns",
                df.shape[1]
            )

        with c3:

            st.metric(
                "❓ Missing",
                int(df.isnull().sum().sum())
            )

        with c4:

            st.metric(
                "🗑 Duplicates",
                int(df.duplicated().sum())
            )

        st.divider()

        st.subheader("📋 Dataset Preview")

        st.dataframe(
            df.head(10),
            width="stretch"
        )

# ============================================================
# DATA CLEANING
# ============================================================

elif menu == "🧹 Data Cleaning":

    st.header("🧹 Data Cleaning")

    if "df" not in st.session_state:

        st.warning(
            "⚠ Please upload a dataset first."
        )

    else:

        st.success(
            "Dataset Ready for Cleaning ✅"
        )

        data_cleaning(
            st.session_state["df"]
        )

# ============================================================
# VISUALIZATION
# ============================================================

elif menu == "📊 Visualization":

    st.header("📊 Data Visualization")

    if "df" not in st.session_state:

        st.warning(
            "⚠ Please upload a dataset first."
        )

    else:

        st.success(
            "Interactive Charts Ready 📈"
        )

        visualization(
            st.session_state["df"]
        )

# ============================================================
# AI ASSISTANT
# ============================================================

elif menu == "🤖 AI Assistant":

    st.header("🤖 Smart Data Assistant")

    st.write(
        "Ask questions related to your uploaded dataset."
    )

    if "df" not in st.session_state:

        st.warning(
            "⚠ Please upload a dataset first."
        )

    else:

        ai_assistant(
            st.session_state["df"]
        )
# ============================================================
# REPORT GENERATOR
# ============================================================

elif menu == "📄 Report Generator":

    st.header("📄 Report Generator")

    st.write(
        "Generate a complete summary report of your dataset."
    )

    if "df" not in st.session_state:

        st.warning(
            "⚠ Please upload a dataset first."
        )

    else:

        st.success(
            "Report Ready to Generate 📄"
        )

        report_generator(
            st.session_state["df"]
        )

# ============================================================
# SIDEBAR FOOTER
# ============================================================

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
### 🚀 AI Data Analyst

Professional Analytics Platform
"""
)

st.sidebar.success("🟢 System Ready")

st.sidebar.info(
    """
Version : **1.0**

Status : **Online**
"""
)

st.sidebar.caption(
    "Powered by Python • Streamlit • Pandas • Plotly"
)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;
padding:18px;
color:#94A3B8;
font-size:15px;">

<b>AI Data Analyst Assistant v1.0</b><br><br>

Developed by <b>Chandana Chadalawada</b><br><br>

Python • Streamlit • Pandas • Plotly

</div>
""",
unsafe_allow_html=True
)