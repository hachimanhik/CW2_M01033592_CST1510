import streamlit as st
from app.data.db import connect_database
from app.data.tickets import get_all_tickets, insert_ticket, delete_ticket

# check login status
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Please login first on Home page.")
    st.stop()

st.title("IT Support Tickets")

# connect to database
conn = connect_database()

# load all tickets
tickets = get_all_tickets(conn)

st.subheader("All tickets")
if len(tickets) == 0:
    st.info("No tickets in database.")
else:
    st.dataframe(tickets)

# delete a ticket
st.subheader("Delete ticket")

delete_id = st.number_input("Ticket ID to delete", min_value=1)

if st.button("Delete ticket"):
    delete_ticket(conn, delete_id)
    st.success("Ticket deleted.")
    st.rerun()

# add new ticket
st.subheader("Add new ticket")

ticket_id = st.number_input("Ticket ID", min_value=1)
priority = st.selectbox("Priority", ["Low", "Medium", "High"])
description = st.text_area("Description")
status = st.selectbox("Status", ["Open", "Closed"])
assigned_to = st.text_input("Assigned to")
created_at = st.text_input("Created at (YYYY-MM-DD)")
resolution_time_hours = st.number_input("Resolution time (hours)", min_value=0.0)

if st.button("Save ticket"):
    insert_ticket(
        conn,
        ticket_id,
        priority,
        description,
        status,
        assigned_to,
        created_at,
        resolution_time_hours
    )
    st.success("Ticket created.")
    st.rerun()

# close connection
conn.close()
