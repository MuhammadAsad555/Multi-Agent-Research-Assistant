from langgraph.graph import StateGraph, END

from state import ResearchState

from agents.research_agent import research_agent
from agents.pdf_agent import pdf_agent
from agents.summarize_agent import summarize_agent
from agents.rag_agent import rag_agent
from agents.memory_agent import memory_agent
from agents.fact_agent import fact_agent
from agents.report_agent import report_agent
from agents.citation_agent import citation_agent
from agents.slides_agent import slides_agent


def build_graph():

    workflow = StateGraph(ResearchState)

    workflow.add_node("memory", memory_agent)
    workflow.add_node("research", research_agent)
    workflow.add_node("pdf", pdf_agent)
    workflow.add_node("summarize", summarize_agent)
    workflow.add_node("rag", rag_agent)
    workflow.add_node("fact", fact_agent)
    workflow.add_node("report", report_agent)
    workflow.add_node("citation", citation_agent)
    workflow.add_node("slides", slides_agent)

    workflow.set_entry_point("memory")

    workflow.add_edge("memory", "research")
    workflow.add_edge("research", "pdf")
    workflow.add_edge("pdf", "summarize")
    workflow.add_edge("summarize", "rag")
    workflow.add_edge("rag", "fact")
    workflow.add_edge("fact", "report")
    workflow.add_edge("report", "citation")
    workflow.add_edge("citation", "slides")
    workflow.add_edge("slides", END)

    return workflow.compile()