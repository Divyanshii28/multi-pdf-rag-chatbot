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
        st.write(pdf.name)


if uploaded_files:
    st.success(f"{len(uploaded_files)} PDF(s) uploaded successfully!")

    for pdf in uploaded_files:
        st.subheader(f"📄 {pdf.name}")

        reader = PdfReader(pdf)

        st.write(f"Pages: {len(reader.pages)}")

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        st.text_area(
            "Preview",
            text[:1000],
            height=200
        )