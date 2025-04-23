# 🧠 Lazy-Agent

**A GPT-powered agent for on-demand legal code retrieval** from Spanish Fork’s Municipal Code GitHub repository.

## 🚀 Overview

`lazy-agent` is a lightweight Retrieval-Augmented Generation (RAG) framework that uses GitHub as its dynamic knowledge base. It is optimized for question-answering on structured documents like municipal codes, legal ordinances, or technical chapters — fetching only what’s needed, when it’s needed.

### ⚙️ How It Works

- A user submits a natural language question  
- The agent routes the query to the correct Title or Part  
- The agent fetches the relevant HTML file from a GitHub repo (via raw URL)  
- That content is injected into a GPT prompt and used to answer the question  

This keeps resource use efficient and answers focused.

---

## 📁 Repo Structure

```
lazy-agent/
├── app/
│   ├── retriever.py         # Fetch HTML files from GitHub
│   ├── router.py            # Map queries to Title files
│   ├── prompt_builder.py    # Combine query + HTML into a GPT prompt
│   └── main.py              # CLI or API entry point
├── config/
│   └── titles_index.json    # Keyword-to-file map (optional)
├── examples/
│   └── sample_queries.md    # Demo Q&A prompts
├── .env                     # API keys and config
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

---

## 🔍 Example Use Case

**Query:**  
"What are the rules for Accessory Dwelling Units in Spanish Fork?"

**Routing →** `title15_land_use.html`  
**Retrieval →** HTML content for Title 15  
**GPT prompt →** Inject only the needed section  
**Response →** Targeted legal summary with citations

---

## 📦 Dependencies

Install required packages:

```
pip install -r requirements.txt
```

Core dependencies:
- `requests`
- `openai`

Optional enhancements:
- `langchain`
- `llama-index`
- `faiss-cpu`

---

## 🔑 Configuration

Create a `.env` file like this:

```
OPENAI_API_KEY=your-key-here
REPO_RAW_BASE=https://raw.githubusercontent.com/YOUR_ORG/municipal-code/main/titles
```

---

## 🧪 Running Locally

Run the CLI or test a sample query:

```
python app/main.py
```

Or from Python:

```python
from app.lazy_loader import lazy_load_and_answer
print(lazy_load_and_answer("What are the zoning rules for ADUs?"))
```

---

## 🛠️ Roadmap

- [ ] Add semantic chunk-based retrieval  
- [ ] Add support for TOC-based smart routing  
- [ ] Deploy as a web app with Streamlit or FastAPI  
- [ ] Add citation links in responses  

---

## 📜 License

MIT — see `LICENSE`

---

## 🧩 Contributions Welcome

Have ideas to expand this to other cities or legal corpora? Open an issue or pull request!
