import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from chains.resume_chain import analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it against a job description.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Resume Upload")
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:
    st.subheader("Job Description")
    job_description = st.text_area(
        "Paste Job Description",
        height=300
    )

st.divider()

if st.button("🚀 Analyze Resume", use_container_width=True):

    if uploaded_file is None:
        st.error("Please upload a resume PDF.")
        st.stop()

    if not job_description.strip():
        st.error("Please enter a job description.")
        st.stop()

    with st.spinner("Analyzing Resume..."):
        try:
            resume_text = extract_text_from_pdf(uploaded_file)

            st.write("Resume text length:", len(resume_text) if resume_text else 0)
            st.write("Resume preview:", resume_text[:200] if resume_text else "EMPTY")
            st.write("Job desc length:", len(job_description))

            result = analyze_resume(resume_text, job_description)

            st.write("Raw result:", result)
            st.write("Result type:", type(result))

            st.success("Analysis Complete!")
            st.subheader("Results")
            st.write(result)

        except Exception as e:
            st.error(f"Error: {e}")
            import traceback
            st.code(traceback.format_exc())