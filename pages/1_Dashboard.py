import streamlit as st
import pandas as pd

from app.data.db import connect_database
from app.data.incidents import get_all_incidents
from app.data.tickets import get_all_tickets
from app.data.datasets import get_all_datasets

# page setup
st.set_page_config(page_title="Dashboard", layout="wide")

# check login
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("Please login first on Home page.")
    st.stop()

# title
st.title("Dashboard")

# connect to database
conn = connect_database()

# load data from tables
df_incidents = get_all_incidents(conn)
df_tickets = get_all_tickets(conn)
df_datasets = get_all_datasets(conn)

# show total numbers
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Total cyber incidents")
    st.subheader(len(df_incidents))

with col2:
    st.subheader("Total IT tickets")
    st.subheader(len(df_tickets))

with col3:
    st.subheader("Total datasets")
    st.subheader(len(df_datasets))

# incidents bar chart
st.subheader("Incidents by severity")

if not df_incidents.empty:
    sev_count = df_incidents["severity"].value_counts()
    st.bar_chart(sev_count)
else:
    st.info("No incidents found")

# tickets bar chart
st.subheader("Tickets by status")

if not df_tickets.empty:
    status_count = df_tickets["status"].value_counts()
    st.bar_chart(status_count)
else:
    st.info("No tickets found")

# datasets bar chart
st.subheader("Dataset records")

if not df_datasets.empty:
    df_datasets = df_datasets.rename(columns={"rows": "records"})
    chart_data = df_datasets.set_index("name")["records"]
    st.bar_chart(chart_data)
else:
    st.info("No datasets found")
