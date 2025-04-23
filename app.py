from fastapi import FastAPI
from pydantic import BaseModel
from tools.search import search_google
from tools.scrape import scrape_url
from tools.analyze import analyze_text

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/query")
async def query_agent(q: Query):
    urls = search_google(q.question)
    scraped_data = [scrape_url(url) for url in urls[:3]]
    combined_text = "\n".join(scraped_data)
    analysis = analyze_text(combined_text)
    return {"response": analysis}