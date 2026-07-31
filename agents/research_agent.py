from tools.arxiv_tool import search_arxiv

def research_agent(state):
    topic = state.get("topic", "")
    papers = search_arxiv(topic)[:5]
    
    selected_inputs = state.get("selected_papers", [])

    if selected_inputs:
        # Extract the titles safely whether they were passed as strings or dict objects
        selected_titles = []
        for item in selected_inputs:
            if isinstance(item, dict):
                selected_titles.append(item.get("title", ""))
            else:
                selected_titles.append(str(item))

        # Filter the papers list accurately
        papers = [
            p for p in papers 
            if p["title"] in selected_titles
        ]

    citations = []
    for i, paper in enumerate(papers, start=1):
        citations.append(
            f'{i}. "{paper["title"]}" - {", ".join(paper["authors"])}'
        )

    return {
        "papers": papers,
        "citations": citations
    }