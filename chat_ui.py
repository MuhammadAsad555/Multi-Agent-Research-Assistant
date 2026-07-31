import streamlit as st
from tools.llm import llm

def chat_ui(report):
    st.subheader("💬 Ask Questions About the Selected Paper")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Simple layout container using standard components
    user_question = st.text_input(
        "Ask a question about the report or topic:",
        key="chat_input",
        placeholder="e.g., What is supervised learning?"
    )

    if st.button("Ask"):
        if user_question:
            # Context-aware prompting logic
            if report and report != "No paper selected.":
                prompt = f"""
Answer the question using this research report.
REPORT:
{report[:3000]}

QUESTION:
{user_question}
"""
            else:
                prompt = f"""
The user wants to know about a machine learning concept, but no paper report has been generated yet. 
Provide a clear, educational, and accurate definition answering their question.

QUESTION:
{user_question}
"""
            with st.spinner("Thinking..."):
                answer = llm(prompt)

            # Store the chat inside session state to survive page reruns
            st.session_state.chat_history.append({
                "question": user_question,
                "answer": answer
            })

    # Render History Logs chronologically
    if st.session_state.chat_history:
        st.markdown("---")
        for chat in st.session_state.chat_history:
            st.markdown("**Question:**")
            st.write(chat["question"])
            st.markdown("**Answer:**")
            st.write(chat["answer"])
            st.divider()