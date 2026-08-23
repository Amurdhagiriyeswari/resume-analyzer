import pdfplumber

# Extract text from resume PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def clean_text(text):
    return text.lower()

# List of skills we check for
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

# Step 1: Get resume skills
resume_text = clean_text(extract_text_from_pdf("sample_resume.pdf"))
resume_skills = find_skills(resume_text, SKILLS_LIST)

# Step 2: Job description (you can change this text to any job posting)
job_description = """
We are looking for a Software Developer with strong skills in Python,
SQL, Git, and React. Experience with Machine Learning and Data Analysis
is a plus. Familiarity with Excel and Tableau is helpful.
"""
job_text = clean_text(job_description)
job_skills = find_skills(job_text, SKILLS_LIST)

# Step 3: Compare
matched_skills = [skill for skill in resume_skills if skill in job_skills]
missing_skills = [skill for skill in job_skills if skill not in resume_skills]

match_percentage = round((len(matched_skills) / len(job_skills)) * 100, 2) if job_skills else 0

# Step 4: Print results
print("Resume Skills:", resume_skills)
print("Job Requires:", job_skills)
print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)
print(f"Match Percentage: {match_percentage}%")