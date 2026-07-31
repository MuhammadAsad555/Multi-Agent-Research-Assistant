import streamlit as st
from tools.llm import llm

def chat_ui(context):

    st.subheader("AI Research Chat")

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    user_input = st.chat_input("Ask follow-up question")

    if user_input:

        prompt = f"""
Use this research report:

{context}

Answer question:
{user_input}
"""

        response = llm(prompt)

        st.session_state.chat_messages.append(("user", user_input))
        st.session_state.chat_messages.append(("assistant", response))

    for role, msg in st.session_state.chat_messages:
        with st.chat_message(role):
            st.write(msg)