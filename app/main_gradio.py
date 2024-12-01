import gradio as gr
import os
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

llm = Chain()
portfolio = Portfolio()

def generate_mail(url_input):
    try:
        loader = WebBaseLoader(web_paths=[url_input])
        cleaned_page = clean_text(loader.load().pop().page_content)
        portfolio.load_portfolio()
        jobs = llm.extract_job(cleaned_page)
        

        email_outputs = []
        for job in jobs:
            skills = job.get("skills", [])
            links = portfolio.query_links(skills=skills)
            email = llm.generate_mail(job=job, links=links)
            email_outputs.append(email)

        return "\n\n".join(email_outputs)
    
    except Exception as e:
        return f"Error: {str(e)}"
    

def create_gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# 📩 Outreach Mail Generator")
        url_input = gr.Textbox(label="Enter a URL:", value="https://gopay.co.id/karier/job/data-scientist-intern-indonesia")
        submit_button = gr.Button("Generate Mail")
        email_output = gr.Textbox(label="Generated Mail", interactive=False, lines=10)
        submit_button.click(generate_mail, inputs=url_input, outputs=email_output)

    return demo

if __name__ == "__main__":
    app = create_gradio_interface()
    app.launch()
