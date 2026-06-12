# AI Resume Analyzer

AI Resume Analyzer is a Streamlit-based web application that analyzes a candidate's resume against a job description using Mistral AI and LangChain.

## Features

* Upload Resume PDF
* Extract Resume Text Automatically
* Compare Resume with Job Description
* ATS-Style Analysis
* Resume Summary
* Strengths and Weaknesses
* Missing Skills Detection
* Interview Question Suggestions
* Modern Streamlit User Interface

## Tech Stack

* Python
* Streamlit
* LangChain
* Mistral AI
* PyPDF
* Python Dotenv

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── .env
│
├── chains/
│   └── resume_chain.py
│
├── prompts/
│   └── resume_prompt.py
│
├── utils/
│   └── pdf_reader.py
│
└── outputs/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/arshadzohaib/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

## How It Works

1. Upload a PDF resume.
2. Paste a job description.
3. The application extracts text from the resume.
4. Mistral AI analyzes the resume against the job description.
5. Results are displayed with recommendations and insights.

## Future Improvements

* ATS Score Visualization
* Resume Improvement Suggestions
* Download Analysis Report
* Multi-Resume Comparison
* Support for Multiple AI Models

## Author

Zohaib Arshad
