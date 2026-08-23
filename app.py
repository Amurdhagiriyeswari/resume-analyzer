import streamlit as st
import pdfplumber

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def clean_text(text):
    return text.lower()

SKILLS_LIST = [
    "python", "java", "c++", "javascript", "html", "css",
    "sql", "react", "node.js", "flask", "django",
    "machine learning", "data analysis", "pandas", "numpy",
    "git", "github", "excel", "power bi", "tableau"
]

def find_skills(text, skills_list):
    found = []
    for skill in skills_list:
        if skill in text:
            found.append(skill)
    return found

st.title("Resume Analyzer")
st.write("Upload your resume and paste a job description to see your match score.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_description = st.text_area("Paste the job description here")

if st.button("Analyze"):
    if uploaded_file is not None and job_description.strip() != "":
        resume_text = clean_text(extract_text_from_pdf(uploaded_file))
        resume_skills = find_skills(resume_text, SKILLS_LIST)

        job_text = clean_text(job_description)
        job_skills = find_skills(job_text, SKILLS_LIST)

        matched_skills = [s for s in resume_skills if s in job_skills]
        missing_skills = [s for s in job_skills if s not in resume_skills]
        match_percentage = round((len(matched_skills) / len(job_skills)) * 100, 2) if job_skills else 0

        st.subheader(f"Match Score: {match_percentage}%")
        st.write("**Matched Skills:**", matched_skills)
        st.write("**Missing Skills:**", missing_skills)
    else:
        st.warning("Please upload a resume and enter a job description.")