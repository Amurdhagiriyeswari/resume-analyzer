import streamlit as st
import pdfplumber
import re

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")

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
    "Frontend Developer": ["html", "css", "javascript", "react", "git"],
    "Backend Developer": ["python", "java", "sql", "flask", "django", "git"],
    "Cloud Engineer": ["aws", "azure", "docker", "kubernetes", "cloud computing", "git"],
    "Cybersecurity Analyst": ["python", "sql", "git", "cloud computing", "docker"],
    "Data Analyst": ["sql", "excel", "pandas", "data analysis", "power bi", "tableau"],
}

def find_skills(text, skills_list):
    found = []
    for skill in skills_list:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found.append(skill)
    return found

if "page" not in st.session_state:
    st.session_state.page = "home"

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.header("ℹ️ About")
    st.write("This tool analyzes your resume against job requirements or a target career, and gives you a personalized skill gap report.")
    st.write("Built with Python + Streamlit.")

    if st.session_state.page != "home":
        if st.button("⬅ Back to Home"):
            st.session_state.page = "home"
            st.rerun()

    st.divider()
    st.header("🕒 History")
    if st.session_state.history:
        for entry in reversed(st.session_state.history):
            st.write(f"- {entry}")
        if st.button("Clear History"):
            st.session_state.history = []
            st.rerun()
    else:
        st.write("No analyses yet this session.")

if st.session_state.page == "home":
    st.markdown(
        "<div style='text-align: center; font-size: 60px;'>📄✨</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h1 style='text-align: center; color: #6C63FF; font-size: 48px;'>Resume Analyzer</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 18px; color: gray;'>Find out how well your resume matches a job — or plan your path to a new career.</p>",
        unsafe_allow_html=True
    )
    st.divider()
    st.write("### Choose what you'd like to do:")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("#### 🧾 Resume vs Job Description")
            st.write("Upload your resume and compare it against a specific job posting to get a match score.")
            if st.button("Start Resume Match", use_container_width=True):
                st.session_state.page = "resume"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("#### 🎯 Career Skill Roadmap")
            st.write("Pick a target career and see which skills you already have and which ones you need to learn.")
            if st.button("Start Career Roadmap", use_container_width=True):
                st.session_state.page = "career"
                st.rerun()

    with col3:
        with st.container(border=True):
            st.markdown("#### 📊 Compare All Careers")
            st.write("Select the skills you have and see your match percentage across every career at once.")
            if st.button("Compare All Careers", use_container_width=True):
                st.session_state.page = "compare"
                st.rerun()

elif st.session_state.page == "resume":
    st.title("🧾 Resume vs Job Description")

    with st.container(border=True):
        st.write("Upload your resume and paste a job description to see your match score.")
        uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
        job_description = st.text_area("Paste the job description here")
        analyze_clicked = st.button("Analyze")

    if analyze_clicked:
        if uploaded_file is not None and job_description.strip() != "":
            resume_text = clean_text(extract_text_from_pdf(uploaded_file))
            resume_skills = find_skills(resume_text, SKILLS_LIST)

            with st.container(border=True):
                st.subheader("Resume Strength Tips")

                word_count = len(resume_text.split())

                if "github" in resume_text:
                    st.success("✅ GitHub link/profile mentioned.")
                else:
                    st.warning("⚠️ Add your GitHub profile to showcase your projects.")

                if "certification" in resume_text or "certificate" in resume_text:
                    st.success("✅ Certifications mentioned.")
                else:
                    st.warning("⚠️ Consider adding relevant certifications.")

                if word_count < 200:
                    st.warning("⚠️ Your resume seems short. Consider adding more details about your projects and experience.")
                else:
                    st.success("✅ Resume has a reasonable amount of content.")

            job_text = clean_text(job_description)
            job_skills = find_skills(job_text, SKILLS_LIST)

            matched_skills = [s for s in resume_skills if s in job_skills]
            missing_skills = [s for s in job_skills if s not in resume_skills]
            match_percentage = round(
                (len(matched_skills) / len(job_skills)) * 100, 2
            ) if job_skills else 0

            with st.container(border=True):
                colm1, colm2 = st.columns([1, 3])
                with colm1:
                    st.metric("Match Score", f"{match_percentage}%")
                with colm2:
                    st.progress(int(match_percentage))

                if match_percentage >= 70:
                    st.success("🟢 STRONG MATCH — Your skills closely match this job!")
                elif match_percentage >= 40:
                    st.warning("🟡 MODERATE MATCH — You can improve some skills.")
                else:
                    st.error("🔴 NEEDS PREPARATION — Focus on the missing skills.")

            with st.container(border=True):
                col_a, col_b = st.columns(2)

                with col_a:
                    st.markdown("### ✅ Matched Skills")
                    if matched_skills:
                        for skill in matched_skills:
                            st.markdown(f"- {skill}")
                    else:
                        st.write("None found.")

                with col_b:
                    st.markdown("### 📚 Skills to Learn")
                    if missing_skills:
                        for skill in missing_skills:
                            resource = SKILL_RESOURCES.get(
                                skill,
                                (
                                    "Search online for tutorials",
                                    "https://www.google.com/search?q=" + skill.replace(" ", "+") + "+tutorial"
                                )
                            )
                            st.markdown(f"- **{skill}** → [{resource[0]}]({resource[1]})")
                    else:
                        st.write("None — great job!")

            missing_with_links = []
            for skill in missing_skills:
                resource = SKILL_RESOURCES.get(
                    skill,
                    ("Search online for tutorials", "https://www.google.com/search?q=" + skill.replace(" ", "+") + "+tutorial")
                )
                missing_with_links.append(f"- {skill} -> {resource[0]}: {resource[1]}")

            report_text = f"""RESUME ANALYSIS REPORT
========================
Match Score: {match_percentage}%

Matched Skills:
{chr(10).join(['- ' + s for s in matched_skills]) if matched_skills else 'None'}

Missing Skills & Where to Learn:
{chr(10).join(missing_with_links) if missing_with_links else 'None'}
"""
            st.download_button(
                label="📥 Download Report",
                data=report_text,
                file_name="resume_analysis_report.txt",
                mime="text/plain"
            )

            st.session_state.history.append(f"Resume Match: {match_percentage}%")
        else:
            st.warning("Please upload a resume and enter a job description.")

elif st.session_state.page == "career":
    st.title("🎯 Career Skill Roadmap")

    with st.container(border=True):
        career = st.selectbox("Choose your target career:", list(CAREER_SKILLS.keys()))
        st.write(f"Select the skills you already have for **{career}**:")

        student_skills = []
        for skill in CAREER_SKILLS[career]:
            if st.checkbox(skill.title()):
                student_skills.append(skill)

        gap_clicked = st.button("Show My Gap")

    if gap_clicked:
        required = CAREER_SKILLS[career]
        missing = [s for s in required if s not in student_skills]
        match_pct = round((len(student_skills) / len(required)) * 100, 2)

        with st.container(border=True):
            colm1, colm2 = st.columns([1, 3])
            with colm1:
                st.metric("Match Score", f"{match_pct}%")
            with colm2:
                st.progress(int(match_pct))

            if match_pct >= 70:
                st.success("🟢 STRONG MATCH — You're well prepared for this career!")
            elif match_pct >= 40:
                st.warning("🟡 MODERATE MATCH — Keep building your skills.")
            else:
                st.error("🔴 NEEDS PREPARATION — Learn more of the required skills.")

        with st.container(border=True):
            col_a, col_b = st.columns(2)

            with col_a:
                st.markdown("### ✅ Matched Skills")
                if student_skills:
                    for skill in student_skills:
                        st.markdown(f"- {skill}")
                else:
                    st.write("None selected.")

            with col_b:
                st.markdown("### 📚 Skills to Learn")
                if missing:
                    for skill in missing:
                        resource = SKILL_RESOURCES.get(
                            skill,
                            (
                                "Search online for tutorials",
                                "https://www.google.com/search?q=" + skill.replace(" ", "+") + "+tutorial"
                            )
                        )
                        st.markdown(f"- **{skill}** → [{resource[0]}]({resource[1]})")
                else:
                    st.write("None — great job!")

        missing_with_links_career = []
        for skill in missing:
            resource = SKILL_RESOURCES.get(
                skill,
                ("Search online for tutorials", "https://www.google.com/search?q=" + skill.replace(" ", "+") + "+tutorial")
            )
            missing_with_links_career.append(f"- {skill} -> {resource[0]}: {resource[1]}")

        roadmap_text = f"""CAREER SKILL ROADMAP - {career}
========================
Match Score: {match_pct}%

Skills You Have:
{chr(10).join(['- ' + s for s in student_skills]) if student_skills else 'None'}

Skills To Learn & Where:
{chr(10).join(missing_with_links_career) if missing_with_links_career else 'None'}
"""
        st.download_button(
            label="📥 Download Roadmap",
            data=roadmap_text,
            file_name=f"{career.replace('/', '_')}_roadmap.txt",
            mime="text/plain"
        )

        st.session_state.history.append(f"Career Roadmap ({career}): {match_pct}%")

elif st.session_state.page == "compare":
    st.title("📊 Compare All Careers")

    with st.container(border=True):
        st.write("Select all the skills you currently have:")

        all_skills_flat = sorted(set(skill for skills in CAREER_SKILLS.values() for skill in skills))

        my_skills = []
        cols = st.columns(4)
        for i, skill in enumerate(all_skills_flat):
            with cols[i % 4]:
                if st.checkbox(skill.title(), key=f"compare_{skill}"):
                    my_skills.append(skill)

        compare_clicked = st.button("Compare Against All Careers")

    if compare_clicked:
        with st.container(border=True):
            st.markdown("### 📈 Your Match Across Careers")
            results = []
            for career_name, required_skills in CAREER_SKILLS.items():
                matched = [s for s in required_skills if s in my_skills]
                pct = round((len(matched) / len(required_skills)) * 100, 2)
                results.append((career_name, pct))

            results.sort(key=lambda x: x[1], reverse=True)

            best_career, best_pct = results[0]
            st.success(f"🏆 Best Fit: **{best_career}** ({best_pct}% match)")

            for career_name, pct in results:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.write(f"**{career_name}**")
                with col2:
                    st.progress(int(pct))
                    st.write(f"{pct}%")

        st.session_state.history.append(f"Compared all careers with {len(my_skills)} skills")
