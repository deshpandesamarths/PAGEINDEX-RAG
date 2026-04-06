# 📄 Agentic Vectorless RAG with PageIndex

An end-to-end **Vectorless Retrieval-Augmented Generation (RAG)** system built using **PageIndex** and **LLM integration**, without relying on embeddings or vector databases.

---

## 🚀 Overview

This project demonstrates a modern approach to document question-answering using:

* 🔹 **PageIndex** for structured document indexing
* 🔹 **Agentic / API-based retrieval**
* 🔹 **LLM (Gemini / OpenAI)** for answer generation
* 🔹 **Streamlit UI** for interactive querying

Unlike traditional RAG systems, this approach avoids:

* ❌ Embeddings
* ❌ Vector databases
* ❌ Chunking heuristics

Instead, it leverages **hierarchical document understanding and intelligent retrieval**.

---

## 🧠 Architecture

```
PDF Document
     ↓
PageIndex (Parsing + Tree Structure)
     ↓
Retrieval API (Relevant Sections)
     ↓
LLM (Answer Generation)
     ↓
Streamlit UI
```

---

## ✨ Features

* 📂 Upload PDF documents via UI
* 📊 Automatic document indexing
* 🌳 Tree-based document structure extraction
* 💬 Natural language querying
* ⚡ Fast and context-aware retrieval
* 🔐 Secure API key handling using `.env`

---

## 📁 Project Structure

```
project/
│
├── main.py              # Backend logic (indexing + retrieval + RAG)
├── app.py               # Streamlit frontend
├── requirements.txt     # Dependencies
├── .env                 # API keys (not committed)
│
├── documents/           # Uploaded PDFs (auto-created)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/deshpandesamarths/PAGEINDEX-RAG.git
cd your-folder-path
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Create `.env` file

```
PAGEINDEX_API_KEY=your_pageindex_key
GOOGLE_API_KEY=your_google_key
```

---

### 4️⃣ Run the application

```
streamlit run app.py --server.port 8052
```

---

## 🧪 Usage

1. Upload a PDF document
2. Wait for indexing to complete
3. Ask questions in natural language
4. Get context-aware answers

---

## 📌 Example Queries

* "Summarize the document"
* "What is the main contribution?"
* "Explain the methodology"
* "List all sections in the document"

---

## 🔍 How It Works

* The document is uploaded and sent to PageIndex
* PageIndex builds a structured representation internally
* Queries are processed via retrieval APIs
* Relevant content is passed to the LLM
* Final answers are generated using contextual information

---

## ⚠️ Limitations

* No direct access to internal tree structure (API-based version)
* Indexing time depends on document size
* Requires external API keys

---

## 🚀 Future Improvements

* 🔥 Chat history (multi-turn conversations)
* 🔥 Multi-document querying
* 🔥 UI for visualizing document structure
* 🔥 Highlighting retrieved content in PDF
* 🔥 Hybrid RAG (vector + structure)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve.

---

## 📜 License

This project is for educational and research purposes.

---

## 👨‍💻 Author

Your Name: Samarth S Deshpande
GitHub: https://github.com/deshpandesamarths/PAGEINDEX-RAG
