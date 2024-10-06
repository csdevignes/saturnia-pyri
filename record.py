import streamlit as st

def record():
    # Option to append results to existing file, or create a new result file
    # Form with : date
    # medication : select from previous, dose, qty
    # symptoms : fatigue, pain, mental fog from 1 to 10
    # sleep (night before) : good, average, bad
    # Joint symptoms : time of morning stiffness : select between 0/15/30/45/1h or more
    # articulations affected : list
    # Time of stiffness starting evening
    # Define the format for form saving. json ? jsonl ?
    st.write("Recording")