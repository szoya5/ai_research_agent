import os
import google.generativeai as genai

def analyze_text(text):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize the following:\n{text[:3000]}")
    return response.text