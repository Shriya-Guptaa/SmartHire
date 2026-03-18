# SmartHire
## AI Resume Ranking & Candidate Matching System

##  Overview

This project is an AI-powered resume screening system designed to automate candidate evaluation by analyzing resumes and ranking them based on their relevance to a given job description.

The system processes multiple resumes, extracts key information, computes similarity with the job description, and ranks candidates using a dynamic scoring approach.

---

## Features

* Upload multiple resumes (PDF/DOCX)
* Automatic resume parsing and information extraction
* Dynamic skill extraction from resume content
* Job Description matching using TF-IDF and cosine similarity
* Candidate scoring and ranking
* Interactive dashboard using Streamlit

---

## Screenshots of the working project

![image alt](https://github.com/vertexbuddy-ai-hiring/ai-resume-ranking-and-candidate-matching-system-Shriya-Guptaa/blob/7db90d7d4fd98c948686d87e2476235b5e6ef605/demo/Screenshot%202026-03-18%20115949.png)

![image alt](https://github.com/vertexbuddy-ai-hiring/ai-resume-ranking-and-candidate-matching-system-Shriya-Guptaa/blob/7db90d7d4fd98c948686d87e2476235b5e6ef605/demo/Screenshot%202026-03-18%20120039.png)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/vertexbuddy-ai-hiring/ai-resume-ranking-and-candidate-matching-system-Shriya-Guptaa.git
cd ai-resume-ranking-and-candidate-matching-system-Shriya-Guptaa
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

---

##  Project Structure

```
project/
│
├── app.py          # Streamlit UI
├── screening.py    # Resume parsing & data extraction
├── matching.py     # Similarity computation & ranking logic
├── requirements.txt
└── README.md
```

---

##  File Description

### `app.py` — User Interface

* Handles resume uploads and job description input
* Triggers processing pipeline
* Displays ranked candidates in a structured table

---

### `screening.py` — Resume Screening

* Extracts text from PDF and DOCX resumes
* Identifies:

  * Email
  * Phone number
  * Years of experience
* Dynamically extracts potential skills from resume text
* Converts unstructured resumes into structured data

---

### `matching.py` — Candidate Matching & Ranking

* Converts resume and job description text into vector representations using TF-IDF
* Computes similarity using cosine similarity
* Applies scoring logic to rank candidates
* Returns ranked results

---

##  System Workflow

```
Upload Resumes
      ↓
Screening (Parsing & Extraction)
      ↓
Matching (Similarity + Scoring)
      ↓
Ranking
      ↓
Display Results
```

---

##  Ranking Methodology

The system ranks candidates using a similarity-driven scoring approach:

### 1. Skill & Content Matching

* TF-IDF vectorization is used to represent both resumes and the job description
* Cosine similarity measures how closely a resume aligns with the job requirements
* This approach captures semantic relevance rather than relying only on exact keyword matches

---

### 2. Experience Scoring

* Years of experience are extracted using pattern matching
* Scores are normalized relative to the required experience

---

### 3. Final Score

* The final score is a weighted combination of similarity and experience
* Candidates are ranked in descending order of this score

---

## 📊 Output

The system displays ranked candidates with:

* Name
* Skills
* Experience
* Similarity Score
* Final Score
* Rank

---

##  Design Approach

The system is built using a modular architecture:

* **Screening layer** handles parsing and extraction
* **Matching layer** handles similarity computation and ranking

Instead of relying on predefined skill lists, the system dynamically analyzes resume content and job descriptions, making it adaptable across different domains.


---

## Conclusion

This project demonstrates how NLP techniques and structured scoring can be used to automate resume screening. The system improves efficiency in candidate evaluation while maintaining a clean, modular, and scalable design.

