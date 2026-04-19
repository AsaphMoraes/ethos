STYLES = """
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stSidebar {
        background-color: #1e1e1e;
    }
    .css-1d391kg {
        background-color: #f0f2f6;
    }
    .css-1jxh1h2 {
        background-color: #ffffff;
    }
    .stMetric {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
    }
    .stMetric .stMetricValue {
        font-size: 24px;
        font-weight: bold;
    }
</style>
"""

def apply_styles():
    import streamlit as st
    st.markdown(STYLES, unsafe_allow_html=True)