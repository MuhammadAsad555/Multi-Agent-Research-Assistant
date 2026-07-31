from tools.pdf_reader import read_pdf_from_url


def pdf_agent(state):

    texts = []

    for paper in state["papers"]:

        text = read_pdf_from_url(paper["pdf"])

        if text:
            texts.append(text)

    return {
        "pdf_texts": texts
    }