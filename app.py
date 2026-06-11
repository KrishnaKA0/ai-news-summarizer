import streamlit as st
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# 1. Load the AI Text Summarizer (Lightweight & Fast)
@st.cache_resource
def load_ai():
    return pipeline("summarization", model="t5-small")

summarizer = load_ai()

# 2. The Dynamic Web Scraper
def fetch_live_news():
    url = "https://news.ycombinator.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = soup.find_all('span', class_='titleline')
    articles = []
    
    for link in links[:10]: # Grabs the top 10 live tech articles
        a_tag = link.find('a')
        if a_tag:
            articles.append({"title": a_tag.text, "url": a_tag['href']})
    return articles

# 3. The Web Interface
st.title("📰 Real-Time AI News Summarizer")
st.markdown("This app dynamically scrapes live headlines and processes them using a local AI Transformer model.")

if st.button("Fetch & Summarize Live News", type="primary"):
    with st.spinner("Scraping live data and running NLP analysis..."):
        news = fetch_live_news()
        
        if news:
            # Combine headlines into one block of text for the AI to read
            text_to_summarize = ". ".join([art['title'] for art in news])
            
            # Run AI Summarization
            ai_output = summarizer(text_to_summarize, max_length=100, min_length=30, do_sample=False)
            summary_paragraph = ai_output[0]['summary_text']
            
            # Display Results
            st.subheader("🤖 Executive Summary")
            st.success(summary_paragraph)
            
            st.subheader("🎯 Scraped Live Links")
            for idx, art in enumerate(news, 1):
                st.markdown(f"**{idx}.** [{art['title']}]({art['url']})")