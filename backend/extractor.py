import fitz  # PyMuPDF
from docx import Document
import os


def extract_text(file_path):
    """
    Extract text from PDF or DOCX file.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        text = ""
        pdf = fitz.open(file_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()
        return text

    elif extension == ".docx":
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text

    else:
        raise ValueError("Only PDF and DOCX files are supported.")


if __name__ == "__main__":
    file = input("Enter resume path: ")

    try:
        resume_text = extract_text(file)

        print("\n========== RESUME TEXT ==========\n")
        print(resume_text)

    except Exception as e:
        print(f"Error: {e}")