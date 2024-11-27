# 📩 Outreach Mail Generator

Outreach Mail Generator is a tool that helps companies to generate outreach emails using Groq, LangChain, and Streamlit/Gradio. It enables users to input the URL of a company's careers page, extract job postings from it, and create personalized emails. These emails incorporate relevant portfolio links retrieved from a vector database, customized to align with specific job descriptions.

### Scenario:

Albert, a leading company in the manufacturing sector, is looking for a **Machine Learning Engineer** (ML Engineer) or a **Data Scientist**. They are investing time and resources in the hiring process, onboarding, and training new employees.  
**MichCorp**, an innovative AI & Software Consulting company, can provide a dedicated software development engineer or data science expert to Albert. So, the business development executive from MichCorp reaches out to Albert by generating a personalized email.

---

## Set-up

To get started, follow these steps:

1. **Get API_KEY:**
   Obtain your API key from here: [https://console.groq.com/keys](https://console.groq.com/keys). Once you have it, create a `.env` file inside the app directory and update the `GROQ_API_KEY` with the value of your API key.

2. **Install Dependencies:**
   Install the required dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App:**
   Once dependencies are installed, you can run the Streamlit app using the command below:

   ```bash
   streamlit run app/main_streamlit.py
   ```

4. **Run the Gradio App:**
   Alternatively, you can run the Gradio app by using the following command:

   ```bash
   python app/main_gradio.py
   ```

---

## Usage

1. **Streamlit App:**
   - The Streamlit interface allows you to input the URL of a company's careers page. It will extract job listings and generate personalized outreach emails.

2. **Gradio App:**
   - The Gradio interface provides a similar user experience, allowing users to input the URL of a company's careers page and generating personalized cold emails with the relevant portfolio links.

---

### File structure:

```
app/
├── main_streamlit.py    # Streamlit version of the Outreach Mail Generator
├── main_gradio.py       # Gradio version of the Outreach Mail Generator
├── .env                 # Contains GROQ_API_KEY for accessing Groq API
├── requirements.txt     # List of required Python packages
└── img.png              # Architecture diagram image
```

---
