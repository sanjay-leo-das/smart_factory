import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Smart Sewing Industrial Platform", layout="wide")

# ---------- GLOBAL STYLE ----------
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: "Times New Roman", Times, serif;
}

.main {
    background: linear-gradient(to right, #000814, #001d3d);
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #ffffff;
    text-shadow: 0px 0px 25px #00f7ff;
    margin-top: 40px;
}

.status-box {
    margin: 40px auto;
    width: 70%;
    text-align: center;
    padding: 20px;
    border-radius: 20px;
    background-color: #2b3a67;
    box-shadow: 0px 0px 30px #00f7ff;
    font-size: 20px;
}

.button-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 70px;
    margin-top: 60px;
}

.custom-btn {
    background-color: transparent;
    color: white;
    border: 2px solid #00f7ff;
    padding: 12px 35px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s ease-in-out;

    /* 🔥 ALWAYS GLOW */
    box-shadow: 0px 0px 15px #00f7ff;
}

.custom-btn:hover {
    background-color: #00f7ff;
    color: black;
    box-shadow: 0px 0px 30px #00f7ff;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">SMART SEWING INDUSTRIAL PLATFORM</div>', unsafe_allow_html=True)

# ---------- TIME & STATUS ----------
now = datetime.now()
current_time = now.strftime("%d/%m/%Y | %I:%M %p")
hour = now.hour

if 9 <= hour < 18:
    status = '<span style="color:lime;">WORK TIME</span>'
elif hour >= 18:
    status = '<span style="color:yellow;">OVERTIME</span>'
else:
    status = '<span style="color:red;">CLOSED</span>'

st.markdown(f'<div class="status-box">{current_time} | {status}</div>', unsafe_allow_html=True)

# ---------- BUTTONS ----------
# ---------- BUTTON STYLE ----------
st.markdown("""
<style>
div.stButton > button {
    background-color: transparent;
    color: white;
    border: 2px solid #00f7ff;
    padding: 14px 40px;
    border-radius: 15px;
    font-size: 16px;
    font-weight: bold;
    box-shadow: 0px 0px 20px #00f7ff;
    transition: 0.3s ease-in-out;
}

div.stButton > button:hover {
    background-color: #00f7ff;
    color: black;
    box-shadow: 0px 0px 40px #00f7ff;
}
</style>
""", unsafe_allow_html=True)

# ---------- CENTER BUTTON LAYOUT ----------
col_space1, col1, col2, col3, col_space2 = st.columns([1,2,2,2,1])

with col1:
    if st.button("🏠 HOME", use_container_width=True):
        st.switch_page("app.py")

with col2:
    if st.button("GO TO MACHINE ANALYTICS", use_container_width=True):
        st.switch_page("pages/1_Machine_Analytics.py")

with col3:
    if st.button("COMPLAINTS", use_container_width=True):
        st.switch_page("pages/3_Complaints.py")
