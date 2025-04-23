import os
import requests
from dotenv import load_dotenv

load_dotenv()
REPO_RAW_BASE = os.getenv("REPO_RAW_BASE")

def fetch_html_from_github(filename: str) -> str:
    url = f"{REPO_RAW_BASE}/{filename}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching file from GitHub: {url}")
    return response.text