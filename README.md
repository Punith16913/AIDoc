# AIDoc – Technical Documentation Intelligence Assistant 🤖📄

**AIDoc** is a production-ready Generative AI application built with Python, LangChain, FAISS, and Google Gemini. It allows users to upload technical documentation, manuals, or API specs (in PDF or TXT format) and ask questions in natural language. Answers are grounded in the document's content using **Retrieval-Augmented Generation (RAG)** to eliminate hallucinations.

---

## ✨ Features
* **Document Ingestion:** Upload and parse any `.pdf` or `.txt` document effortlessly.
* **Vector Embeddings:** Uses Google's `text-embedding-004` to create dense semantic representations.
* **High-Speed Vector Search:** Employs **FAISS** (Facebook AI Similarity Search) for sub-second retrieval of relevant chunks.
* **Grounded Synthesized Answers:** Powered by `gemini-2.5-flash` to ensure strict reliance on source material.
* **Transparent Citations:** Expandable UI component showing exact source chunks used for each answer.
* **Clean UI:** Streamlit interface for simple, interactive query testing.

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **LLM & Embeddings** | Google Gemini (`gemini-2.5-flash` & `text-embedding-004`) |
| **Framework** | LangChain / LangChain-Community |
| **Vector DB** | FAISS |
| **Frontend UI** | Streamlit |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- A Google Gemini API Key ([Get a free key here](https://aistudio.google.com/))

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/AIDoc.git](https://github.com/your-username/AIDoc.git)
   cd AIDoc