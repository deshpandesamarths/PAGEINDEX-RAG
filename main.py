import os
import time
from dotenv import load_dotenv
from pageindex import PageIndexClient
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- INIT CLIENT ----------------
pi_client = PageIndexClient(
    api_key=os.getenv("PAGEINDEX_API_KEY")
)

# ---------------- INIT LLM ----------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
)

# ---------------- UPLOAD + INDEX ----------------
def upload_and_index(pdf_path):
    doc_info = pi_client.submit_document(pdf_path)
    doc_id = doc_info["doc_id"]

    # wait until ready
    while not pi_client.is_retrieval_ready(doc_id):
        time.sleep(2)

    return doc_id

# ---------------- RETRIEVE ----------------
def retrieve_from_pageindex(query, doc_id, top_k=3):

    response = pi_client.submit_query(
        doc_id=doc_id,
        query=query
    )

    retrieval_id = response.get("retrieval_id")

    while True:
        retrieval = pi_client.get_retrieval(retrieval_id)
        status = retrieval.get("status")

        if status == "completed":
            break
        elif status == "failed":
            return []

        time.sleep(1)

    nodes = retrieval.get("retrieved_nodes", [])
    contexts = []

    for node in nodes[:top_k]:
        for group in node.get("relevant_contents", []):
            for item in group:
                content = item.get("relevant_content")
                if content:
                    contexts.append(content)

    return contexts

# ---------------- RAG ----------------
def vectorless_rag(query, doc_id):

    contexts = retrieve_from_pageindex(query, doc_id)

    if not contexts:
        return "No relevant context found."

    combined_context = "\n\n".join(contexts)

    prompt = f"""
    Answer ONLY using the context below.

    Context:
    {combined_context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content