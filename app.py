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
"python", "java", "c++", "c", "javascript", "html", "css",
"sql", "react", "node.js", "flask", "django",
"machine learning", "data analysis", "pandas", "numpy",
"git", "github", "excel", "power bi", "tableau",
"prompt engineering", "generative ai", "chatgpt", "llm",
"large language models", "artificial intelligence", "deep learning",
"nlp", "natural language processing", "tensorflow", "pytorch",
"ai tools", "openai", "hugging face", "langchain",
"computer vision", "data science", "cloud computing",
"aws", "azure", "docker", "kubernetes"
]
SKILL_RESOURCES = {
"python": "freeCodeCamp - Python Course",
"java": "Oracle Java Tutorials",
"sql": "W3Schools SQL Tutorial",
"react": "React Official Docs",
"machine learning": "Coursera - Andrew Ng's ML Course",
"data analysis": "Kaggle Learn - Data Analysis",
"excel": "Microsoft Excel Training",
"git": "GitHub Learning Lab",
"tableau": "Tableau Public Training",
"power bi": "Microsoft Power BI Learning",
"prompt engineering": "DeepLearning.AI - Prompt Engineering Course",
"generative ai": "Google Cloud Skills Boost - Generative AI",
"llm": "DeepLearning.AI - LLM courses",
"nlp": "Coursera - NLP Specialization",
"deep learning": "DeepLearning.AI - Deep Learning Specialization",
"aws": "AWS Skill Builder (free tier)",
"docker": "Docker Official Getting Started Guide"
}

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
        st.write("**Missing Skills & Suggested Resources:**")
        for skill in missing_skills:
         resource = SKILL_RESOURCES.get(skill, "Search online for tutorials")
        st.write(f"- **{skill}** → {resource}")

else:
    st.warning("Please upload a resume and enter a job description.")
