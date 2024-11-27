import streamlit as st
import os
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def StreamlitApp(llm, portfolio, clean_text):
    st.title("📩 Reachout Mail Generator")
    url_input = st.text_input("Enter a URL:",value="https://gopay.co.id/karier/job/data-scientist-intern-indonesia")
    submit_button = st.button("Generate Mail")

    if submit_button:
        try:
            loader = WebBaseLoader(web_paths=[url_input])
            cleaned_page = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs =llm.extract_job(cleaned_page)
            for job in jobs:
                skiils = job.get("skills", [])
                links = portfolio.query_links(skills=skiils)
                email = llm.generate_mail(job=job, links=links)
                st.code(email, language="markdown")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    llm = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="📩 Rreachout Mail Generator")
    StreamlitApp(llm, portfolio, clean_text)
        