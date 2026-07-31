from tools.llm import llm

def fact_agent(state):

    context = state.get("rag_context", "").strip()

    if not context:
        return {
            "verified_report": ""
        }

    prompt = f"""
Clean and organize the following research notes.

Research:
{context}
"""

    verified = llm(prompt)

    return {
        "verified_report": verified
    }