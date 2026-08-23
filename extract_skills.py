import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def clean_text(text):
    return text.lower()

SKILLS_LIST = [
    "python", "java", "c++", "c", "javascript", "html", "css",
    "sql", "react", "node.js", "flask", "django",
    "machine learning", "data analysis", "pandas", "numpy",
    "git", "github", "excel", "power bi", "tableau"
]

def find_skills(resume_text, skills_list):
    found_skills = []
    for skill in skills_list:
        if skill in resume_text:
            found_skills.append(skill)
    return found_skills

resume_text = extract_text_from_pdf("sample_resume.pdf")
cleaned_text = clean_text(resume_text)
matched_skills = find_skills(cleaned_text, SKILLS_LIST)

print("Skills found in resume:")
print(matched_skills)