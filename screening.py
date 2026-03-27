import pdfplumber
import docx
import re


def extract_text(file):
    text = ""

    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text



def extract_name(text):
    lines = text.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line:
            return line
    return "Unknown"


def extract_email(text):
    match = re.findall(r'\S+@\S+', text)
    return match[0] if match else "N/A"


def extract_phone(text):
    match = re.findall(r'\d{10}', text)
    return match[0] if match else "N/A"

def extract_experience(text):
    match = re.findall(r'(\d+)\s*(?:years?|yrs?)', text.lower())
    return int(match[0]) if match else 0


def extract_skills(text):
    skills = []

    match = re.search(r"skills[:\-]?\s*(.+)", text, re.IGNORECASE)

    if match:
        skills_text = match.group(1)
        skills = [s.strip() for s in skills_text.split(",")]

    return skills



def parse_resumes(uploaded_files):
    resumes_data = []

    for file in uploaded_files:
        text = extract_text(file)

        resumes_data.append({
            "name": extract_name(text),
            "text": text,
            "email": extract_email(text),
            "phone": extract_phone(text),
            "experience": extract_experience(text),
            "skills": extract_skills(text)
        })

    return resumes_data