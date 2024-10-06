import streamlit as st

from record import record
from visualize import visualize

def page_selection_ff(selected_func):
    mapping = {record : "Record", visualize : "Visualize"}
    return mapping[selected_func]

page_selection = st.radio("Mode", [record, visualize], format_func=page_selection_ff, key="page-selection", horizontal=True)

page_selection()