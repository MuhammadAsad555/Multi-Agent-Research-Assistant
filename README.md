# 🔬 Multi-Agent Research Assistant

An AI-powered research platform that automates the academic research workflow using multiple specialized AI agents.

The application searches research papers from arXiv, retrieves relevant documents, performs Retrieval-Augmented Generation (RAG), summarizes findings, verifies facts, generates citations, and produces structured reports and presentation slides—all through a modern Streamlit interface.

---

## ✨ Features

- 🔍 Search research papers from arXiv
- 🤖 Multi-Agent architecture
- 📄 PDF processing
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Semantic search using vector embeddings
- 📝 AI-generated research summaries
- ✅ Fact verification
- 📖 Automatic citation generation
- 📊 Progress tracking
- 💬 Interactive chat interface
- 📑 Research report generation
- 📽️ PowerPoint presentation generation
- 🎨 Modern Streamlit UI

---

## 🏗️ Project Structure

```
Multi_Agent_Researcher/
│
├── agents/
│   ├── research_agent.py
│   ├── summarize_agent.py
│   ├── report_agent.py
│   ├── citation_agent.py
│   ├── rag_agent.py
│   ├── fact_agent.py
│   ├── memory_agent.py
│   └── slides_agent.py
│
├── tools/
│   ├── arxiv_tool.py
│   ├── llm.py
│   ├── pdf_reader.py
│   └── vector_store.py
│
├── ui/
│   ├── chat.py
│   ├── progress.py
│   └── styles.css
│
├── outputs/
├── app.py
├── graph.py
├── config.py
├── state.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

- Python
- Streamlit
- LangGraph
- LangChain
- OpenAI / Groq
- ChromaDB
- HuggingFace Embeddings
- arXiv API

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Multi_Agent_Researcher.git
```

Move into the project

```bash
cd Multi_Agent_Researcher
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

Example:

```env
OPENAI_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

1. User enters a research topic.
2. Research Agent searches arXiv.
3. PDFs are downloaded.
4. PDF Reader extracts text.
5. Vector Store creates embeddings.
6. RAG Agent retrieves relevant context.
7. Summarization Agent generates summaries.
8. Citation Agent formats references.
9. Fact Agent validates important claims.
10. Report Agent generates the final report.
11. Slides Agent creates a PowerPoint presentation.

---

## 📌 Future Improvements

- GitHub integration
- Multi-LLM support
- Memory persistence
- PDF report export
- Agent analytics dashboard
- Multi-document comparison
- Research timeline visualization

---

## 📄 License

This project is intended for educational and portfolio purposes.