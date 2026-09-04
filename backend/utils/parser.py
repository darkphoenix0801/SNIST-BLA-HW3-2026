import io
import pdfplumber
import docx

def parse_resume_file(file_content: bytes, filename: str) -> str:
    """
    Extracts text from a resume file (PDF or DOCX).
    """
    text = ""
    file_like = io.BytesIO(file_content)

    if filename.lower().endswith(".pdf"):
        with pdfplumber.open(file_like) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    elif filename.lower().endswith(".docx"):
        doc = docx.Document(file_like)
        for para in doc.paragraphs:
            text += para.text + "\n"
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are supported.")

    return text.strip()
