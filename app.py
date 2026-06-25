import streamlit as st
from src.pdf_loader import extract_text_from_pdfs
from src.text_splitter import get_text_chunks

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

    extracted_text = extract_text_from_pdfs(uploaded_files)

    st.write(f"**Extracted Characters:** {len(extracted_text)}")

    chunks = get_text_chunks(extracted_text)

    st.write(f"**Total Chunks Created:** {len(chunks)}")

    with st.expander("Preview extracted text"):
        st.text_area("Text Preview", extracted_text[:1500], height=250)

    with st.expander("Preview text chunks"):
        for i, chunk in enumerate(chunks[:3]):
            st.markdown(f"### Chunk {i + 1}")
            st.write(chunk)
            