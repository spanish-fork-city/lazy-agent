from flask import Flask, request, jsonify
from app.router import get_relevant_filename
from app.retriever import fetch_html_from_github
from app.prompt_builder import build_prompt

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "Missing 'question' in request"}), 400

    try:
        filename = get_relevant_filename(question)
        html_content = fetch_html_from_github(filename)
        prompt = build_prompt(question, html_content)

        return jsonify({
            "question": question,
            "filename": filename,
            "prompt": prompt
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)