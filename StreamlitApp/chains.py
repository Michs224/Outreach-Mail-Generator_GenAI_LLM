from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import os

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            model_name="llama-3.3-70b-versatile",
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        
    def extract_job(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scrapped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: 'role', 'experience', 'skills', and 'description'.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_text})
        
        try:
            json_parses = JsonOutputParser()
            json_res = json_parses.parse(res.content)
        except OutputParserException as e:
            raise Exception(f"Error parsing output: {str(e)}")
        return json_res if isinstance(json_res, list) else [json_res]
    
    def generate_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}
                
                ### INSTRUCTION:
                You are Michael, a business development executive at MichCorp. MichCorp is an innovative AI & Software Consulting company, specializing in the development of advanced technological solutions that empower businesses to optimize their operations. With a focus on leveraging cutting-edge AI technologies, MichCorp works closely with clients to enhance automation, streamline workflows, and drive business growth. Our solutions have helped numerous organizations achieve greater operational efficiency, cost savings, and scalability.

                Your job is to write a cold email to the client regarding the job mentioned above, showcasing MichCorp's expertise in meeting their needs. 
                Additionally, please include the most relevant portfolio items from the following links: {link_list}
                Remember, you are Michael, BDE at MichCorp. 
                Do not provide a preamble.
                ### EMAIL (NO PREAMBLE):
                
                """
        )

        chain_extract = prompt_email | self.llm
        res = chain_extract.invoke(input={'job_description': str(job), 'link_list': links})
        return res.content
        
if __name__ == "__main__":
    pass