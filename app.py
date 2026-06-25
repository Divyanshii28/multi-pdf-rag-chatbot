import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="Multi-PDF RAG Chatbot",
    page_icon="📚"
)

st.title("📚 Multi-PDF RAG Chatbot")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} PDF(s) uploaded successfully!")

    for pdf in uploaded_files:
        st.subheader(f"📄 {pdf.name}")

        reader = PdfReader(pdf)
        number_of_pages = len(reader.pages)

        st.write(f"**Total Pages:** {number_of_pages}")

        extracted_text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text

        st.write(f"**Extracted Characters:** {len(extracted_text)}")

        with st.expander("Preview extracted text"):
            st.text_area(
                "Text Preview",
                extracted_text[:1500],
                height=250
            )