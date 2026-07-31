from tools.vector_store import create_index, search_index

def rag_agent(state):

    summaries = state.get("summaries", [])

    if len(summaries) == 0:

        return {
            "rag_context": ""
        }

    index, texts = create_index(summaries)

    query = state.get("topic", "")

    retrieved = search_index(index, texts, query)

    return {
        "rag_context": "\n".join(retrieved)
    }