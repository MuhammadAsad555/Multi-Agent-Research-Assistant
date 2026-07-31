import requests
from pypdf import PdfReader
import io


def read_pdf_from_url(url):

    try:
        response = requests.get(url)

        pdf = PdfReader(io.BytesIO(response.content))

        text = ""

        for page in pdf.pages:
            text += page.extract_text()

        return text

    except:
        return ""