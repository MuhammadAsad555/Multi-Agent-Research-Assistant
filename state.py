from typing import TypedDict, List, Dict


class ResearchState(TypedDict, total=False):

    topic: str

    selected_papers: List[Dict]

    papers: List[Dict]

    pdf_texts: List[str]

    summaries: List[str]

    rag_context: str

    verified_report: str

    report: str

    citations: List[str]

    slides: str

    memory: List[str]