from tools.llm import llm

def summarize_agent(state):
    papers = state.get("selected_papers", [])
    summaries = []

    for paper in papers:
        # Safely handle if paper comes in as a string or dict object
        if isinstance(paper, str):
            paper_title = paper
            paper_authors = []
            paper_summary = ""
        else:
            paper_title = paper.get('title', '')
            paper_authors = paper.get('authors', [])
            paper_summary = paper.get('summary', '')

        text = f"""
Title:
{paper_title}

Authors:
{', '.join(paper_authors)}

Summary:
{paper_summary}
"""

        prompt = f"""
You are a research assistant.

Create a detailed summary ONLY for this paper.

{text}

Include:
- Research Problem
- Methodology
- Findings
- Limitations
- Future Work

Do NOT invent information.
"""

        summary = llm(prompt)
        summaries.append(summary)

    return {
        "summaries": summaries
    }