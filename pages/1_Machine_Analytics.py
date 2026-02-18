import streamlit as st

st.set_page_config(page_title="Machine Analytics", layout="wide")

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>

/* BACK BUTTON GLOW */
div.stButton > button {
    border-radius: 15px;
    border: 2px solid cyan;
    box-shadow: 0 0 15px cyan;
    font-weight: bold;
    transition: 0.3s;
}
div.stButton > button:hover {
    box-shadow: 0 0 30px cyan;
    transform: scale(1.05);
}

/* CARD STYLE BUTTON */
.machine-card button {
    background: linear-gradient(145deg,#111,#1b1f2a);
    color: white;
    padding: 35px;
    border-radius: 20px;
    border: 2px solid cyan;
    box-shadow: 0 0 25px cyan;
    text-align: left;
    font-size: 18px;
    height: 220px;
    transition: 0.3s;
}
.machine-card button:hover {
    box-shadow: 0 0 40px cyan;
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# ---------- BACK BUTTON ----------
col1, col2 = st.columns([1, 8])
with col1:
    if st.button("← BACK"):
        st.switch_page("dashboard.py")

# ---------- TITLE ----------
st.markdown("""
<style>

/* BACK BUTTON GLOW */
div.stButton > button {
    border-radius: 15px;
    border: 2px solid cyan;
    box-shadow: 0 0 15px cyan;
    font-weight: bold;
    transition: 0.3s;
}
div.stButton > button:hover {
    box-shadow: 0 0 30px cyan;
    transform: scale(1.05);
}

/* CARD STYLE BUTTON */
.machine-card button {
    background: linear-gradient(145deg,#111,#1b1f2a);
    color: white;
    padding: 40px 25px;   /* height increase */
    border-radius: 25px;
    border: 2px solid cyan;
    box-shadow: 0 0 25px cyan;
    text-align: center;
    font-size: 22px;      /* text bigger */
    height: 260px;        /* more height */
    max-width: 320px;     /* width shorter */
    margin: auto;         /* center card */
    transition: 0.3s;
}

.machine-card button:hover {
    box-shadow: 0 0 40px cyan;
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)


# ---------- MACHINE DATA ----------
machines = [
    {"name": "MACHINE 1", "serial": "M001", "status": "IDLE", "breaks": 8},
    {"name": "MACHINE 2", "serial": "M002", "status": "IDLE", "breaks": 7},
    {"name": "MACHINE 3", "serial": "M003", "status": "IDLE", "breaks": 7},
    {"name": "MACHINE 4", "serial": "M004", "status": "RUNNING", "breaks": 8},
    {"name": "MACHINE 5", "serial": "M005", "status": "RUNNING", "breaks": 7},
    {"name": "MACHINE 6", "serial": "M006", "status": "RUNNING", "breaks": 6},
]

# ---------- CARD GRID ----------
rows = [machines[i:i+3] for i in range(0, len(machines), 3)]

for row in rows:
    cols = st.columns(3)
    for col, machine in zip(cols, row):
        with col:
            st.markdown('<div class="machine-card">', unsafe_allow_html=True)

            if st.button(
                f"""
### {machine['name']}

Serial No: {machine['serial']}

Status: {machine['status']}

Thread Breaks: {machine['breaks']}
                """,
                key=machine["serial"],
                use_container_width=True
            ):
                st.session_state.selected_machine = machine["name"]
                st.switch_page("pages/2_Detailed_Analytics.py")

            st.markdown('</div>', unsafe_allow_html=True)

    st.write("")

