import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        texts = soup.stripped_strings
        content = " ".join(texts)
        return content[:5000]
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"