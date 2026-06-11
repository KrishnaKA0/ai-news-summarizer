import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

# 1. High-Performance Heuristic Summarizer
def generate_summary(text_data, articles):
    if not articles:
        return "No articles available to summarize."
    
    keywords = ["AI", "Tech", "Software", "Launch", "Code", "System", "Open Source", "Data", "Web", "Cybersecurity", "Linux"]
    found_tags = [w for w in keywords if w.lower() in text_data.lower()]
    
    summary_sentence = f"⚡ Today's top tech insights focus heavily on tracking developments across **{', '.join(found_tags[:4]) if found_tags else 'emerging software architectures'}**.\n\n"
    summary_sentence += f"🔥 The core focus centers around the leading trending development: *'{articles[0]['title']}'*, followed closely by secondary community movements tracking *'{articles[1]['title'] if len(articles) > 1 else 'open infrastructure design'}'*."
    
    return summary_sentence

# 2. The Dynamic Web Scraper
def fetch_live_news():
    url = "https://news.ycombinator.com/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('span', class_='titleline')
        articles = []
        for link in links[:12]: 
            a_tag = link.find('a')
            if a_tag:
                articles.append({"title": a_tag.text, "url": a_tag['href']})
        return articles
    except Exception as e:
        return []

# 3. Premium Web Interface Design
st.set_page_config(page_title="PulseAI News Intel", page_icon="⚡", layout="wide")

# Custom CSS styling banner (Fixed keyword syntax)
st.markdown("""
    <div style="background: linear-gradient(90deg, #1f4068, #162447); padding: 20px; border-radius: 10px; margin-bottom: 25px; border-left: 8px solid #e43f5a;">
        <h1 style="color: white; margin: 0; font-family: 'Helvetica Neue', sans-serif;">⚡ PulseAI News Intel</h1>
        <p style="color: #cbd5e1; margin: 5px 0 0 0; font-size: 1.1rem;">Dynamic Web Scraper & Contextual Executive Summarization Engine</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Control Room
st.sidebar.markdown("### 🎛️ Control Panel")
st.sidebar.markdown("Click the button below to trigger the dynamic scraping pipeline and run the NLP engine.")
run_pipeline = st.sidebar.button("🚀 Run Live Pipeline", type="primary", use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.caption("🤖 Powered by Python, BeautifulSoup4, and Streamlit Cloud.")

if run_pipeline:
    with st.spinner("Executing scraper requests & processing structural insights..."):
        news = fetch_live_news()
        
        if news:
            text_to_summarize = ". ".join([art['title'] for art in news])
            summary_paragraph = generate_summary(text_to_summarize, news)
            
            # Interactive KPI Metrics Banner
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.metric(label="Target Source Feed", value="HackerNews")
            with col_m2:
                st.metric(label="Live Records Parsed", value=f"{len(news)} Stories")
                
            st.markdown("---")
            
            # --- TWO-COLUMN DASHBOARD LAYOUT ---
            left_col, right_col = st.columns([1, 1], gap="large")
            
            with left_col:
                st.markdown("### 🤖 Cognitive AI Summary")
                st.info(summary_paragraph)
                
            with right_col:
                st.markdown("### 🎯 Curated Live Feed")
                for idx, art in enumerate(news, 1):
                    st.markdown(f"""
                        <div style="background-color: #1a1a2e; padding: 12px; border-radius: 6px; margin-bottom: 8px; border-bottom: 2px solid #1f4068;">
                            <strong style="color: #e43f5a;">{idx}.</strong> 
                            <a href="{art['url']}" target="_blank" style="color: #cbd5e1; text-decoration: none; font-weight: 500;">{art['title']}</a>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("🚨 Connection timeout. Target server did not respond. Please try running the pipeline again.")
else:
    st.markdown("""
        <div style="text-align: center; padding: 60px 20px; color: #64748b; background-color: #0f172a; border-radius: 8px; border: 1px dashed #334155;">
            <span style="font-size: 3rem;">📥</span>
            <h3 style="margin-top: 15px; color: #94a3b8;">The Intelligence Feed is Idle</h3>
            <p>Please launch the automated pipeline from the left <b>Control Panel</b> to collect real-time tech insights.</p>
        </div>
    """, unsafe_allow_html=True)
