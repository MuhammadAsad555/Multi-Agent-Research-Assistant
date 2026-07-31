from tools.llm import llm

def report_agent(state):
    papers = state.get("papers", [])

    if not papers:
        return {
            "report": "No paper selected."
        }

    paper = papers[0]

    prompt = f"""
Create a research report ONLY from this paper.

Title:
{paper.get('title', 'Unknown')}

Authors:
{', '.join(paper.get('authors', []))}

Summary:
{paper.get('summary', 'No summary payload provided.')}

STRICT RULE:
Do not invent information.
Do not use any other topic.
Use only this paper.

Include:
1. Title
2. Abstract
3. Key Findings
4. Methodology
5. Conclusion
6. Future Work
"""

    report = llm(prompt)

    return {
        "report": report
    }