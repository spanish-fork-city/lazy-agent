def build_prompt(question: str, html_content: str) -> str:
    return f"""You are a legal assistant. Use the municipal code below to answer the question.

Municipal Code Content:
-----------------------
{html_content}

Question: {question}
Answer:
"""