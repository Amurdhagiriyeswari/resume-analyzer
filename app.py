import streamlit as st
import pdfplumber
import re

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
    "python": ("freeCodeCamp - Python Course", "https://www.freecodecamp.org/learn/scientific-computing-with-python/"),
    "java": ("Oracle Java Tutorials", "https://docs.oracle.com/javase/tutorial/"),
    "sql": ("W3Schools SQL Tutorial", "https://www.w3schools.com/sql/"),
    "react": ("React Official Docs", "https://react.dev/learn"),
    "machine learning": ("Coursera - Andrew Ng's ML Course", "https://www.coursera.org/specializations/machine-learning-introduction"),
    "data analysis": ("Kaggle Learn - Data Analysis", "https://www.kaggle.com/learn/pandas"),
    "excel": ("Microsoft Excel Training", "https://support.microsoft.com/en-us/excel"),
    "git": ("GitHub Learning Lab", "https://docs.github.com/en/get-started"),
    "tableau": ("Tableau Public Training", "https://public.tableau.com/en-us/s/resources"),
    "power bi": ("Microsoft Power BI Learning", "https://learn.microsoft.com/en-us/power-bi/"),
    "prompt engineering": ("DeepLearning.AI - Prompt Engineering Course", "https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/"),
    "generative ai": ("Google Cloud Skills Boost - Generative AI", "https://www.cloudskillsboost.google/paths/118"),
    "llm": ("DeepLearning.AI - LLM courses", "https://www.deeplearning.ai/courses/"),
    "nlp": ("Coursera - NLP Specialization", "https://www.coursera.org/specializations/natural-language-processing"),
    "deep learning": ("DeepLearning.AI - Deep Learning Specialization", "https://www.deeplearning.ai/courses/deep-learning-specialization/"),
    "aws": ("AWS Skill Builder (free tier)", "https://skillbuilder.aws/"),
    "docker": ("Docker Official Getting Started Guide", "https://docs.docker.com/get-started/"),
    "hugging face": ("Hugging Face - Official Course", "https://huggingface.co/course"),
    "openai": ("OpenAI API Documentation & Quickstart Guide", "https://platform.openai.com/docs/quickstart"),
    "langchain": ("LangChain Official Documentation", "https://python.langchain.com/docs/introduction/"),
    "computer vision": ("OpenCV Official Tutorials", "https://docs.opencv.org/master/d9/df8/tutorial_root.html"),
    "data science": ("Kaggle Learn - Data Science", "https://www.kaggle.com/learn"),
    "cloud computing": ("AWS Cloud Practitioner Essentials (free)", "https://skillbuilder.aws/exam-prep/cloud-practitioner"),
    "kubernetes": ("Kubernetes Official Basics Tutorial", "https://kubernetes.io/docs/tutorials/kubernetes-basics/"),
    "chatgpt": ("OpenAI ChatGPT Documentation", "https://help.openai.com/en/collections/3742473-chatgpt"),
    "artificial intelligence": ("Google AI - Machine Learning Crash Course", "https://developers.google.com/machine-learning/crash-course"),
    "tensorflow": ("TensorFlow Official Tutorials", "https://www.tensorflow.org/tutorials"),
    "pytorch": ("PyTorch Official Tutorials", "https://pytorch.org/tutorials/")
}

CAREER_SKILLS = {
    "Data Scientist": ["python", "sql", "pandas", "numpy", "machine learning", "data analysis", "git"],
    "Web Developer": ["html", "css", "javascript", "react", "node.js", "git", "sql"],
    "AI/ML Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch", "nlp", "git"],
}

def find_skills(text, skills_list):
    found = []
    for skill in skills_list:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found.append(skill)
    return found

st.title("Resume Analyzer")

mode = st.radio("Choose Mode:", ["Resume vs Job Description", "Career Skill Roadmap"])

if mode == "Resume vs Job Description":
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
                resource = SKILL_RESOURCES.get(skill, ("Search online for tutorials", "https://www.google.com/search?q=" + skill.replace(" ", "+") + "+tutorial"))
                st.write(f"- **{skill}** → [{resource[0]}]({resource[1]})")
        else:
            st.warning("Please upload a resume and enter a job description.")

elif mode == "Career Skill Roadmap":
    career = st.selectbox("Choose your target career:", list(CAREER_SKILLS.keys()))
    st.write(f"Select the skills you already have for **{career}**:")

    student_skills = []
    for skill in CAREER_SKILLS[career]:
        if st.checkbox(skill.title()):
            student_skills.append(skill)

    if st.button("Show My Gap"):
        required = CAREER_SKILLS[career]
        missing = [s for s in required if s not in student_skills]
        match_pct = round((len(student_skills) / len(required)) * 100, 2)

        st.subheader(f"Skill Match: {match_pct}%")
        st.write("**Missing Skills:**")
        for skill in missing:
            resource = SKILL_RESOURCES.get(skill, ("Search online for tutorials", "https://www.google.com/search?q=" + skill.replace(" ", "+") + "+tutorial"))
            st.write(f"- **{skill}** → [{resource[0]}]({resource[1]})")
