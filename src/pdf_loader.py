from pypdf import PdfReader

def extract_text_from_pdfs(uploaded_files):
    all_text = ""

    for pdf in uploaded_files:
        reader = PdfReader(pdf)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                all_text += page_text + "\n"

    return all_text