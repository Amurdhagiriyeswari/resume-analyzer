# Resume Analyzer

A multi-feature web application that helps students and job seekers understand their skill gaps and plan career growth.

## Live Demo
[resume-analyzer-amurdha.streamlit.app](https://resume-analyzer-amurdha.streamlit.app)

## What You Get
Upload a resume or select your skills, and instantly receive:

- ✅ **A Match Score** (0-100%) showing how well you fit a job or career
- ✅ **Matched Skills** — what you already bring to the table
- ✅ **Missing Skills** — exactly what's needed but not yet on your resume/profile
- ✅ **Real Learning Resources** — each missing skill comes with a direct link to a course or tutorial (freeCodeCamp, Coursera, official docs, etc.) — not just a generic Google search
- ✅ **Resume Strength Tips** — quick feedback on GitHub links, certifications, and resume length
- ✅ **Downloadable Reports** — save your full analysis as a text file

## Three Ways to Analyze

1. **🧾 Resume vs Job Description** — Upload your resume and paste a job posting to get a match score, missing skills, and improvement tips.
2. **🎯 Career Skill Roadmap** — Pick a target career and check off the skills you already have to see your readiness and what to learn next.
3. **📊 Compare All Careers** — Select your skills once and instantly see your match percentage across multiple career paths, with your best-fit career highlighted.

## How It Works
1. User selects a mode from the home page
2. For resume-based analysis: the app extracts and cleans text from the uploaded PDF, then checks it against a predefined skill list using word-boundary regex matching (avoiding false positives)
3. For career-based modes: the app compares user-selected skills against predefined skill requirements for each career
4. Matched and missing skills are computed, along with a match percentage
5. Missing skills are paired with curated learning resources and clickable links
6. Results can be downloaded as a text report

## Tech Stack
- **Python** — core logic
- **Streamlit** — web interface and interactivity
- **pdfplumber** — PDF text extraction
- **re (regex)** — accurate, word-boundary skill matching

## Additional Features
- Skill detection across 40+ technical and AI-related skills (Python, SQL, Machine Learning, Prompt Engineering, Generative AI, etc.)
- Color-coded feedback (strong / moderate / needs preparation)
- Session history tracking
- Clean, card-based, dark-themed interface with home page navigation

## Running Locally
```bash
git clone https://github.com/Amurdhagiriyeswari/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
streamlit run app.py
```
## Project Structure

```text
resume-analyzer/
├── .streamlit/
│   └── config.toml
├── app.py                  # Main application
├── compare_job.py          # Job comparison logic
├── extract_skills.py      # Skill extraction
├── read_resume.py         # Resume reading
├── requirements.txt       # Python dependencies
├── sample_resume.pdf      # Sample resume for testing
└── README.md
```
## Future Improvements
- Smarter skill extraction using NLP/LLMs instead of keyword matching
- Support for multiple resume formats (DOCX)
- Persistent history using a database instead of session-only storage
- Weighted skill importance per career
- Broader job-role suggestions without needing a pasted job description
## Author
Built by Amurdhagiriyeswari
