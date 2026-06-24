import streamlit as st

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