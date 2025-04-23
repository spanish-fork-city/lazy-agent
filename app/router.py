import json
import re
from pathlib import Path

# Load the index
with open(Path(__file__).parent.parent / "titles_index_full.json") as f:
    TITLES_INDEX = json.load(f)

def clean_and_tokenize(text):
    return set(re.findall(r'\b\w+\b', text.lower()))

def get_relevant_filename(question: str) -> str:
    tokens = clean_and_tokenize(question)
    scores = []

    for filename, data in TITLES_INDEX.items():
        keywords = set(map(str.lower, data.get("keywords", [])))
        score = len(tokens & keywords)
        scores.append((score, filename))

    scores.sort(reverse=True)
    top_score, top_file = scores[0]
    return top_file if top_score > 0 else "title01_general_provisions.html"
