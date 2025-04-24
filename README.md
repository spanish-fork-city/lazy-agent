# 🧠 Lazy-Agent — GPT-Powered Municipal Code Assistant

**Lazy-Agent** is a lightweight Retrieval-Augmented Generation (RAG) system built to help GPT models answer legal and regulatory questions about the **Spanish Fork Municipal Code** by **selectively loading only the relevant document** from a structured GitHub repository.

---

## 🎯 Purpose

To create a fast, efficient, and modular assistant that:
- Understands a natural language question
- Determines the correct Title, chapter, or document to reference
- Loads that file from GitHub (on demand — "lazy loading")
- Formats the content into a GPT-readable prompt
- Prepares the system to answer highly specific queries with minimal token cost

---

## 🔧 Key Components

| Component | Purpose |
|----------|---------|
| `titles_index_full.json` | Maps keywords to document paths (Titles, Construction Standards, Public Works) |
| `router.py` | Analyzes the question and selects the best file |
| `retriever.py` | Fetches the raw HTML file from GitHub |
| `prompt_builder.py` | Builds a clean GPT prompt using the question + content |
| `main.py` | CLI tool for testing routing, retrieval, and prompt generation |
| `app.py` | Flask API version to integrate with frontends or GPTs |
| Google Colab notebook | Hosted, no-install version to test routing and prompt creation in the cloud |

---

## ✅ Features

- 🗂 Supports full Title 1–15 structure, plus Construction & Public Works documents
- 🔎 Keyword-based routing using a dynamic JSON index
- 🌐 GitHub-based lazy loading (only fetches what’s needed)
- 🔤 Prompt formatting for GPT models
- 🧪 Fully testable in Google Colab or locally
- 🔌 Modular design for easy integration into web apps or GPT tools

---

## 🧪 Sample Question Flow

**User asks:**  
> “What are the zoning rules for accessory dwelling units?”

1. `router.py` selects `title_15_land_use.html`
2. `retriever.py` fetches it from GitHub
3. `prompt_builder.py` creates:
   ```
   You are a legal assistant. Use the following municipal code to answer:
   [Title 15 content here...]
   Question: What are the zoning rules for accessory dwelling units?
   ```

---

## 🚀 Ready for:
- GPT integration (OpenAI, Claude, or local LLMs)
- Expansion to other city codes or legal documents
- Frontend display with citation support
