from langchain_core.prompts import PromptTemplate

resume_prompt = PromptTemplate(
    input_variables=["resume", "job_description"],
    template="""
Analyze this resume:

{resume}

Job Description:

{job_description}

Give:
1. ATS Score
2. Resume Summary
3. Strengths
4. Weaknesses
5. Missing Skills
6. Interview Questions
"""
)