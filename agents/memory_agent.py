def memory_agent(state):

    memory = state.get("memory", [])

    memory.append(state["topic"])

    return {
        "memory": memory
    }