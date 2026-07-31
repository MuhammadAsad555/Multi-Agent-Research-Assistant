import streamlit as st


def sidebar():

    st.sidebar.title("Multi-Agent Research Assistant")

    topic = st.sidebar.text_input(
        "Enter Research Topic"
    )

    run = st.sidebar.button("Run Agents")

    return topic, run