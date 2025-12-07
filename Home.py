import streamlit as st
from app.data.db import connect_database
from app.data.schema import create_tables, load_csv_if_empty
from app.services.user_services import register_user, login_user


import streamlit as st

st.set_page_config(
    page_title="Intelligence Platform",
    page_icon="app/logo/barcelona.png"
)

# create database tables and load CSV files (runs only once)
create_tables()
load_csv_if_empty()

st.title("Welcome to Multi-Domain Intelligence Platform!")

# session flag for login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# show login + register page if user is not logged in
if not st.session_state.logged_in:

    st.subheader("Register")
    new_user = st.text_input("Enter username")
    new_pass = st.text_input("Enter password", type="password")

    if st.button("Sign up"):
        if register_user(new_user, new_pass):
            st.success("Account created.")
        else:
            st.error("User already exists.")

    st.subheader("Login")
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(user, pw):
            st.session_state.logged_in = True
            st.success("Logged in.")

            # go to Dashboard after login
            st.switch_page("pages/1_Dashboard.py")

        else:
            st.error("Wrong login or password.")

# if logged in, show message and logout button
else:
    st.success("You are logged in.")
    st.write("Use the menu on the left to open other pages.")

    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()
