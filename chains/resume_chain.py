from dotenv import load_dotenv
import os
from langchain_mistralai import ChatMistralAI
from prompts.resume_prompt import resume_prompt

load_dotenv()

def analyze_resume(resume_text, job_description):
    
    api_key = os.getenv("MISTRAL_API_KEY")
    
    print("API KEY FOUND:", api_key is not None)
    print("API KEY VALUE:", api_key[:10] if api_key else "MISSING")
    
    if not api_key:
        return "ERROR: MISTRAL_API_KEY not found in .env file"
    
    try:
        model = ChatMistralAI(
            model="mistral-small-latest",
            api_key=api_key
        )

        prompt = resume_prompt.format(
            resume=resume_text,
            job_description=job_description
        )

        result = model.invoke(prompt)
        
        print("RESULT:", result)
        print("CONTENT:", result.content if result else "None")
        
        if result is None:
            return "ERROR: Model returned None"
        
        return result.content
        
    except Exception as e:
        print("ERROR IN CHAIN:", str(e))
        return f"ERROR: {str(e)}"