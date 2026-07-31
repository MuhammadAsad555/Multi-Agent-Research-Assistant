import streamlit as st
from graph import build_graph
from chat_ui import chat_ui

st.set_page_config(
    page_title="Multi-Agent Autonomous Research Assistant",
    page_icon="🗂️",
    layout="wide"
)

# ----------------------------------------------------------------------------
# THEME
# A quiet "research dossier" palette — slate-navy surfaces, parchment-gold
# accent, serif masthead for headings, clean sans for body copy.
# Medium-depth theme: not stark black, not white.
# ----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {
    --bg-primary:   #1b2430;
    --bg-secondary: #212b38;
    --bg-card:      #263241;
    --border:       #39485a;
    --border-soft:  #2e3b4a;
    --accent-gold:  #c9a15f;
    --accent-gold-soft: #e3c791;
    --accent-blue:  #7fa8d1;
    --text-primary: #eef1f5;
    --text-muted:   #93a3b8;
    --text-faint:   #6b7a8e;
}

/* base canvas */
.stApp {
    background: linear-gradient(180deg, var(--bg-primary) 0%, #19212c 100%);
    color: var(--text-primary);
}
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* kill default streamlit chrome noise */
#MainMenu, footer {visibility: hidden;}
header[data-testid="stHeader"] {background: transparent;}
.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 980px;
}

/* ---------------- masthead ---------------- */
.dossier-masthead {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding-bottom: 1.6rem;
    margin-bottom: 2.2rem;
    border-bottom: 1px solid var(--border);
}
.dossier-eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: 0.22em;
    font-size: 0.72rem;
    text-transform: uppercase;
    color: var(--accent-gold);
    margin-bottom: 0.6rem;
}
.dossier-title {
    font-family: 'Fraunces', serif;
    font-weight: 600;
    font-size: 2.6rem;
    line-height: 1.1;
    color: var(--text-primary);
    margin: 0;
}
.dossier-subtitle {
    font-family: 'Inter', sans-serif;
    color: var(--text-muted);
    font-size: 0.95rem;
    margin-top: 0.7rem;
    max-width: 560px;
}
.dossier-rule {
    width: 64px;
    height: 2px;
    background: var(--accent-gold);
    margin-top: 1rem;
    border-radius: 2px;
}

/* ---------------- section labels ---------------- */
.section-eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--accent-blue);
    margin-bottom: 0.35rem;
}
h2, h3 {
    font-family: 'Fraunces', serif !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
}

/* ---------------- inputs ---------------- */
.stTextInput input {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text-primary) !important;
    padding: 0.7rem 0.9rem !important;
    font-size: 0.95rem !important;
}
.stTextInput input:focus {
    border-color: var(--accent-gold) !important;
    box-shadow: 0 0 0 1px var(--accent-gold) !important;
}
.stTextInput label, .stSelectbox label {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    color: var(--text-muted) !important;
}

div[data-baseweb="select"] > div {
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text-primary) !important;
}

/* ---------------- buttons ---------------- */
.stButton > button {
    background: var(--accent-gold) !important;
    color: #1b2430 !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.4rem !important;
    letter-spacing: 0.01em;
    transition: all 0.15s ease-in-out;
}
.stButton > button:hover {
    background: var(--accent-gold-soft) !important;
    color: #14202b !important;
    transform: translateY(-1px);
}
.stButton > button:active {
    transform: translateY(0px);
}

.stDownloadButton > button {
    background: transparent !important;
    color: var(--accent-blue) !important;
    border: 1px solid var(--accent-blue) !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
}
.stDownloadButton > button:hover {
    background: rgba(127, 168, 209, 0.12) !important;
}

/* ---------------- paper index cards ---------------- */
.paper-card {
    background: var(--bg-card);
    border: 1px solid var(--border-soft);
    border-left: 3px solid var(--accent-gold);
    border-radius: 10px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
}
.paper-number {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.14em;
    color: var(--accent-gold);
    text-transform: uppercase;
    margin-bottom: 0.35rem;
}
.paper-title {
    font-family: 'Fraunces', serif;
    font-weight: 600;
    font-size: 1.25rem;
    color: var(--text-primary);
    margin: 0 0 0.5rem 0;
}
.paper-meta {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-bottom: 0.3rem;
}
.paper-meta a {
    color: var(--accent-blue);
    text-decoration: none;
}
.paper-meta a:hover {
    text-decoration: underline;
}
.paper-summary {
    font-size: 0.92rem;
    color: var(--text-primary);
    opacity: 0.9;
    line-height: 1.55;
    margin-top: 0.5rem;
}

/* ---------------- report / citations panel ---------------- */
.report-panel {
    background: var(--bg-card);
    border: 1px solid var(--border-soft);
    border-radius: 10px;
    padding: 1.6rem 1.8rem;
    line-height: 1.65;
    font-size: 0.96rem;
}
.citation-chip {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.82rem;
    color: var(--text-muted);
    background: var(--bg-secondary);
    border: 1px solid var(--border-soft);
    border-radius: 6px;
    padding: 0.5rem 0.8rem;
    margin-bottom: 0.4rem;
}

/* misc */
hr, .stDivider {
    border-color: var(--border) !important;
}
.stSpinner > div {
    color: var(--accent-gold) !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# MASTHEAD
# ----------------------------------------------------------------------------
st.markdown("""
<div class="dossier-masthead">
    <div class="dossier-eyebrow">Autonomous Research Division</div>
    <h1 class="dossier-title">Multi-Agent Research Assistant</h1>
    <div class="dossier-subtitle">
        Search the arXiv archive, review candidate papers, and compile a
        structured analysis report — end to end, agent-assisted.
    </div>
    <div class="dossier-rule"></div>
</div>
""", unsafe_allow_html=True)

# Initializing Session States safely
if "papers" not in st.session_state:
    st.session_state.papers = None

if "final_result" not in st.session_state:
    st.session_state.final_result = None

st.markdown('<div class="section-eyebrow">Step 01 — Define scope</div>', unsafe_allow_html=True)
topic = st.text_input("Research Topic", placeholder="e.g. retrieval-augmented generation for scientific QA")

# --- 1. SEARCH PAPERS ---
if st.button("Run Research") and topic:
    with st.spinner("Searching arXiv archives..."):
        graph = build_graph()
        temp_result = graph.invoke({
            "topic": topic
        })
        st.session_state.papers = temp_result.get("papers", [])
        st.session_state.final_result = None  # Reset report state on a brand new topic search

# --- 2. SHOW PAPERS ---
if st.session_state.papers:
    papers = st.session_state.papers

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-eyebrow">Step 02 — Review candidates</div>', unsafe_allow_html=True)
    st.subheader("Research Papers")

    for i, paper in enumerate(papers):
        st.markdown(f"""
        <div class="paper-card">
            <div class="paper-number">No. {i+1:02d}</div>
            <div class="paper-title">{paper['title']}</div>
            <div class="paper-meta"><strong>Authors:</strong> {', '.join(paper['authors'])}</div>
            <div class="paper-meta"><strong>PDF:</strong> <a href="{paper['pdf']}" target="_blank">{paper['pdf']}</a></div>
            <div class="paper-summary">{paper['summary']}</div>
        </div>
        """, unsafe_allow_html=True)

    # Create mapping dictionary mapping titles to paper payloads
    paper_map = {paper["title"]: paper for paper in papers}

    st.markdown('<div class="section-eyebrow">Step 03 — Select for deep analysis</div>', unsafe_allow_html=True)
    selected_title = st.selectbox(
        "Select ONE paper for report generation",
        options=list(paper_map.keys())
    )

    if st.button("Generate Report"):
        with st.spinner("Compiling analysis report..."):
            graph = build_graph()
            selected_paper_object = paper_map[selected_title]

            # Pass the extracted title string inside the selected_papers list
            # to keep your internal research_agent filter from zeroing out results
            final_result = graph.invoke({
                "topic": topic,
                "selected_papers": [selected_title]
            })

            st.session_state.final_result = final_result
            st.rerun()

# --- 3. SHOW FINAL RESULT ---
report_for_chat = ""

if st.session_state.final_result:
    result = st.session_state.final_result

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-eyebrow">Step 04 — Findings</div>', unsafe_allow_html=True)

    if "citations" in result and result["citations"]:
        st.subheader("Citations")
        for citation in result["citations"]:
            st.markdown(f'<div class="citation-chip">{citation}</div>', unsafe_allow_html=True)

    if "report" in result and result["report"]:
        st.subheader("Final Research Report")
        st.markdown(f'<div class="report-panel">{result["report"]}</div>', unsafe_allow_html=True)
        report_for_chat = result["report"]

    if "slides" in result and result["slides"]:
        st.subheader("Slides Generated")
        try:
            with open(result["slides"], "rb") as f:
                st.download_button(
                    "Download Slides",
                    data=f,
                    file_name="research_slides.pptx",
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )
        except Exception as e:
            st.error(str(e))

# --- 4. ALWAYS VISIBLE CHATBOT ---
st.divider()
st.markdown('<div class="section-eyebrow">Consult the assistant</div>', unsafe_allow_html=True)
chat_ui(report_for_chat)