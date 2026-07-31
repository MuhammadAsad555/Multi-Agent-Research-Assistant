import streamlit as st


def show_progress():

    st.info("Agents running...")

    progress = st.progress(0)

    for i in range(100):
        progress.progress(i + 1)