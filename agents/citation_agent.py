def citation_agent(state):

    papers = state.get("papers", [])

    citations = []

    for paper in papers:

        citations.append(
            f"{paper['title']} - {', '.join(paper['authors'])}"
        )

    return {
        "citations": citations
    }