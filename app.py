import streamlit as st
import os
from pathlib import Path
from dotenv import load_dotenv

from main import upload_and_index, vectorless_rag

# ---------------- LOAD ENV ----------------
load_dotenv()

DOCUMENTS_DIR = Path("documents")

st.set_page_config(page_title="Vectorless RAG", layout="wide")

st.title("📄 Vectorless RAG (PageIndex + Gemini)")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("📂 Upload PDF", type=["pdf"])

if uploaded_file:

    DOCUMENTS_DIR.mkdir(exist_ok=True)
    pdf_path = DOCUMENTS_DIR / uploaded_file.name

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Uploaded")

    # ---------------- INDEX ----------------
    if "doc_id" not in st.session_state:
        with st.spinner("Indexing document..."):
            st.session_state.doc_id = upload_and_index(pdf_path)

    doc_id = st.session_state.doc_id

    st.success(f"Indexed: {doc_id}")

    # ---------------- QUERY ----------------
    question = st.text_input("Ask a question")

    if st.button("Ask") and question:

        with st.spinner("Thinking..."):
            answer = vectorless_rag(question, doc_id)

        st.markdown("### ✅ Answer")
        st.write(answer)