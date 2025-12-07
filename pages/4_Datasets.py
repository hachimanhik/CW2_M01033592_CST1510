import streamlit as st
import pandas as pd

from app.data.db import connect_database
from app.data.datasets import get_all_datasets, insert_dataset, delete_dataset

# page setup
st.set_page_config(page_title="Datasets", layout="wide")

# check if user is logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.error("Please login first on Home page.")
    st.stop()

# title
st.title("Datasets")

# connect to database
conn = connect_database()

# load datasets
df = get_all_datasets(conn)

st.subheader("All datasets")
st.dataframe(df, use_container_width=True)

# add new dataset
st.subheader("Add new dataset")

name = st.text_input("Dataset name")
records = st.number_input("Number of records", min_value=0, step=1)

if st.button("Add dataset"):
    if name:
        insert_dataset(conn, name, int(records))
        st.success("Dataset added!")
        st.rerun()
    else:
        st.error("Enter dataset name.")

# delete dataset
st.subheader("Delete dataset")

delete_id = st.number_input("Dataset ID to delete", min_value=0, step=1)

if st.button("Delete"):
    delete_dataset(conn, int(delete_id))
    st.success("Dataset deleted!")
    st.rerun()
