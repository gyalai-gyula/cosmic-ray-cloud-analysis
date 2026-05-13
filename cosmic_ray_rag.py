# ============================================
# COSMIC RAY - CLOUD COVER RAG SYSTEM
# ============================================
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# ============================================
# 1. LOAD PAPERS FROM CSV
# ============================================
df = pd.read_csv(r"nasa_ads.csv")
print(f"Papers loaded: {len(df)}")

# ============================================
# 2. CLAUDE ANALYSIS
# ============================================
def analyze_papers(papers_text):
    url = "https://api.anthropic.com/v1/messages"
    
    headers = {
        "Content-Type": "application/json",
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
    }
    
    prompt = f"""
    The following scientific papers are related to the correlation 
    between cosmic ray intensity and cloud cover:
    
    {papers_text}
    
    Please analyze:
    1. What is the current scientific consensus on this topic?
    2. What has changed since 2009 (since Erlykin, Gyalai, Kudela paper)?
    3. Have the results been confirmed or refuted?
    """
    
    body = {
        "model": "claude-sonnet-4-5",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, json=body)
    return response.json()['content'][0]['text']

# ============================================
# 3. MAIN PROGRAM
# ============================================

# Combine papers into text
papers_text = ""
for i, row in df.iterrows():
    if pd.notna(row['abstract']):
        papers_text += f"\n{row['title']} ({row['year']})\n{row['abstract']}\n"

# Run analysis
print("Claude is analyzing the papers...\n")
analysis = analyze_papers(papers_text)
print(analysis)

# Save results
with open('rag_analysis.txt', 'w', encoding='utf-8') as f:
    f.write(analysis)
print("\nSaved: rag_analysis.txt")