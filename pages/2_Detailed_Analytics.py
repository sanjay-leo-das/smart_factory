import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Detailed Analytics", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: "Times New Roman", serif;
}

.main {
    background: linear-gradient(to right, #000814, #001d3d);
}

.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: white;
    text-shadow: 0px 0px 20px #00f7ff;
}

.summary-box {
    background-color: #0d1b2a;
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #00f7ff;
    box-shadow: 0px 0px 20px #00f7ff;
    margin-bottom: 30px;
    font-size: 18px;
    color: white;
}

.stButton > button {
    background-color: transparent;
    color: white;
    border: 2px solid #00f7ff;
    box-shadow: 0px 0px 15px #00f7ff;
}
</style>
""", unsafe_allow_html=True)

# ---------------- BACK BUTTON ----------------
col1, col2 = st.columns([1,6])
with col1:
    if st.button("⬅ BACK"):
        st.switch_page("pages/1_Machine_Analytics.py")

machine_name = st.session_state.get("selected_machine", "MACHINE 1")

st.markdown(f'<div class="title">OVERALL DATA OF {machine_name}</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------------- SELECT DAYS ----------------
duration = st.radio("Select Duration:", ["Past 7 Days", "Past 30 Days"], horizontal=True)

days = 7 if duration == "Past 7 Days" else 30

# ---------------- GENERATE DATA ----------------
dates = []
work_time = []
idle_time = []
overtime = []
thread_break = []

today = datetime.today()

for i in range(days):
    day = today - timedelta(days=days - i - 1)
    dates.append(day.strftime("%d-%b"))

    if day.weekday() == 6:  # Sunday Holiday
        work_time.append(0)
        idle_time.append(0)
        overtime.append(0)
        thread_break.append(0)
    else:
        work_time.append(7)
        idle_time.append(1)
        overtime.append(2 if i % 3 == 0 else 0)
        thread_break.append((i % 4) + 1)

df = pd.DataFrame({
    "Date": dates,
    "Work Time": work_time,
    "Idle Time": idle_time,
    "Overtime": overtime,
    "Thread Breaks": thread_break
})

# ---------------- SUMMARY ----------------
st.markdown(f"""
<div class="summary-box">
Total Thread Break: {sum(thread_break)} <br><br>
Total Work Time: {sum(work_time)} Hours <br>
Total Idle Time: {sum(idle_time)} Hours <br>
Total Overtime: {sum(overtime)} Hours
</div>
""", unsafe_allow_html=True)

# ---------------- LINE CHART ----------------
fig1 = px.line(df, x="Date", y=["Work Time", "Idle Time", "Overtime"],
               title="Work / Idle / Overtime Trend")
st.plotly_chart(fig1, use_container_width=True)

# ---------------- BAR CHART ----------------
fig2 = px.bar(df, x="Date", y="Thread Breaks",
              title="Thread Break Analysis")
st.plotly_chart(fig2, use_container_width=True)

