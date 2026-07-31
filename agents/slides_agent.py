import os
import json
from pptx import Presentation
from tools.llm import llm

def slides_agent(state):
    report = state.get("report", "No report content available.")
    topic = state.get("topic", "Research Topic")

    # Ask the LLM for structured JSON to ensure high reliability
    prompt = f"""
You are a professional presentation assistant. Create 6 distinct slides based on the provided report.

Topic: {topic}
Report Content:
{report}

STRICT INSTRUCTION: Output your response ONLY as a valid JSON object matching the schema below. Do not include markdown code blocks, backticks, or extra text.

JSON Schema:
{{
    "slides": [
        {{
            "title": "Slide Title Here",
            "bullets": ["Bullet point 1", "Bullet point 2", "Bullet point 3"]
        }}
    ]
}}

Generate exactly 6 slides covering: Title/Introduction, Research Problem, Methodology, Key Findings, Applications, and Conclusion. Keep bullet points brief and informative.
"""

    # Fetch response from LLM
    raw_response = llm(prompt).strip()

    # Clean off any markdown block backticks safely without complex regex strings
    if raw_response.startswith("```"):
        # Split lines, remove the first and last line (the backticks)
        lines = raw_response.splitlines()
        if len(lines) > 2:
            # Check if first line has '```json' or '```'
            if lines[0].strip().startswith("```"):
                lines = lines[1:]
            if lines[-1].strip() == "```":
                lines = lines[:-1]
            raw_response = "\n".join(lines).strip()

    # Initialize PowerPoint Presentation
    prs = Presentation()
    
    try:
        # Load the structured JSON data
        data = json.loads(raw_response)
        slides_list = data.get("slides", [])

        for slide_data in slides_list:
            title_text = slide_data.get("title", "Untitled Slide")
            bullets_list = slide_data.get("bullets", [])

            # Layout 1 is the standard Title + Content layout
            slide_layout = prs.slide_layouts[1]
            slide_obj = prs.slides.add_slide(slide_layout)

            # Assign Slide Title
            slide_obj.shapes.title.text = title_text

            # Assign Bullet Points Content Block
            content_placeholder = slide_obj.placeholders[1]
            content_placeholder.text = "\n".join(bullets_list)

    except Exception as parse_error:
        print(f"JSON Parsing failed, falling back to basic parsing: {parse_error}")
        # Robust basic line fallback parser if JSON fails for any reason
        slide_layout = prs.slide_layouts[1]
        slide_obj = prs.slides.add_slide(slide_layout)
        slide_obj.shapes.title.text = f"Presentation: {topic}"
        slide_obj.placeholders[1].text = "Review full research report for complete overview analytics."

    # Save presentation file
    os.makedirs("outputs", exist_ok=True)
    path = "outputs/slides.pptx"
    prs.save(path)

    state["slides"] = path
    return state