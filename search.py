from serpapi import GoogleSearch
import os

def search_google(query):
    params = {
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "engine": "google",
        "num": 5
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return [r["link"] for r in results.get("organic_results", [])]