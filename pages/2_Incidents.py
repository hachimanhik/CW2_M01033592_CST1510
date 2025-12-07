import streamlit as st
from app.data.db import connect_database
from app.data.incidents import get_all_incidents, insert_incident, delete_incident

# check login status
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Please login first on Home page.")
    st.stop()

st.title("Cyber Incidents")

# connect to database
conn = connect_database()

# load all incidents from table
incidents = get_all_incidents(conn)

st.subheader("All incidents")
if len(incidents) == 0:
    st.info("No incidents in database.")
else:
    st.dataframe(incidents)

# delete an incident by ID
st.subheader("Delete incident")

delete_id = st.number_input("Incident ID to delete", min_value=1)

if st.button("Delete incident"):
    delete_incident(conn, delete_id)
    st.success("Incident deleted.")
    st.rerun()

# add a new incident
st.subheader("Add incident")

incident_id = st.number_input("New Incident ID", min_value=1)
timestamp = st.text_input("Timestamp (YYYY-MM-DD)")
severity = st.selectbox("Severity", ["Low", "Medium", "High"])
category = st.text_input("Category")
status = st.text_input("Status")
description = st.text_area("Description")

if st.button("Save incident"):
    insert_incident(conn, incident_id, timestamp, severity, category, status, description)
    st.success("Incident added.")
    st.rerun()

# close connection
conn.close()
