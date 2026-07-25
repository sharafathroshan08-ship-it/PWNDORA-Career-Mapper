import pdfplumber


def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a PDF resume.
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


if __name__ == "__main__":

    path = input("Enter PDF path: ")

    resume = extract_text_from_pdf(path)

    print("=" * 60)
    print("EXTRACTED TEXT")
    print("=" * 60)

    print(resume)