import streamlit as st

if st.button("← BACK"):
    st.switch_page("dashboard.py")

st.markdown("<h2 style='text-align:center;'>COMPLAINTS</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.metric("Complaints Received", 12)

with col2:
    st.metric("Complaints Solved", 9)
