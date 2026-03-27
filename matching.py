from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(resume_texts, jd_text):
    documents = resume_texts + [jd_text]

    vectorizer = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    jd_vector = tfidf_matrix[-1]
    resume_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(resume_vectors, jd_vector)
    return similarities.flatten()



def calculate_score(similarity, experience, required_exp, text):

    # Skill match (50%)
    skill_score = similarity * 50

    # Experience (25%)
    exp_score = min((experience / required_exp) * 25, 25) if required_exp else 0

    # Education (10%)
    if "bachelor" in text.lower() or "btech" in text.lower() or "master" in text.lower():
        edu_score = 10
    else:
        edu_score = 5

    # Location (15%) placeholder
    loc_score = 10

    total = skill_score + exp_score + edu_score + loc_score
    return round(total)


def rank_candidates(resumes_data, jd_text, required_exp):

    resume_texts = [r["text"] for r in resumes_data]

    similarities = compute_similarity(resume_texts, jd_text.lower())

    results = []

    for i, resume in enumerate(resumes_data):
        score = calculate_score(
            similarities[i],
            resume["experience"],
            required_exp,
            resume["text"]
        )

        results.append({
            "Name": resume["name"],
            "Skills": ", ".join(resume["skills"][:3]),
            "Experience": f"{resume['experience']} yrs",
            "Score": score
        })

    return results