import streamlit as st

from utils.dashboard import show_dashboard
from utils.data_loader import show_data_loader
from utils.data_cleaning import show_data_cleaning
from utils.visualization import show_visualization
from utils.ai_assistant import show_ai_assistant
from utils.report_generator import show_report_generator

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

/* Main App */

.stApp{
    background:#050816;
    color:white;
}

.block-container{
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Sidebar */

[data-testid="stSidebar"]{
    background:#020617;
    border-right:1px solid #1E293B;
}

[data-testid="stSidebar"] *{
    color:white;
}

/* Buttons */

.stButton>button{
    background:#16A34A;
    color:white;
    border:none;
    border-radius:12px;
    font-weight:bold;
    width:100%;
}

.stButton>button:hover{
    background:#22C55E;
}

/* Metrics */

[data-testid="metric-container"]{
    background:#111827;
    border:1px solid #1F2937;
    padding:18px;
    border-radius:15px;
}

/* File Uploader */

[data-testid="stFileUploader"]{
    background:#111827;
    border:2px dashed #22C55E;
    border-radius:15px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🤖 AI Data Analyst")

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

st.sidebar.markdown("""
### 👨‍💻 Developed By

**Chandana Chadalawada**


""")

st.sidebar.markdown("---")

st.sidebar.caption("Powered by Python • Streamlit • Pandas • Plotly")

# ============================================================
# DASHBOARD
# ============================================================

if menu == "🏠 Dashboard":

    show_dashboard()

# ============================================================
# UPLOAD DATASET
# ============================================================

elif menu == "📂 Upload Dataset":

    show_data_loader()

# ============================================================
# DATA CLEANING
# ============================================================

elif menu == "🧹 Data Cleaning":

    if "df" not in st.session_state:

        st.warning("⚠ Please upload a dataset first.")

    else:

        show_data_cleaning()

# ============================================================
# VISUALIZATION
# ============================================================

elif menu == "📊 Visualization":

    if "df" not in st.session_state:

        st.warning("⚠ Please upload a dataset first.")

    else:

        show_visualization(st.session_state["df"])

# ============================================================
# AI ASSISTANT
# ============================================================

elif menu == "🤖 AI Assistant":

    if "df" not in st.session_state:

        st.warning("⚠ Please upload a dataset first.")

    else:

        show_ai_assistant(st.session_state["df"])

# ============================================================
# REPORT GENERATOR
# ============================================================

elif menu == "📄 Report Generator":

    if "df" not in st.session_state:

        st.warning("⚠ Please upload a dataset first.")

    else:

        show_report_generator(st.session_state["df"])

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;color:#94A3B8;font-size:15px;padding:10px;">
<b>AI Data Analyst Assistant v1.0</b><br>
Developed by <b>Chandana Chadalawada</b><br><br>
Python • Streamlit • Pandas • Plotly
</div>
""",
unsafe_allow_html=True
)