import streamlit as st
import pandas as pd
from screening import parse_resumes
from matching import rank_candidates


st.set_page_config(page_title="AI Resume Ranking", layout="wide")

st.title("AI Resume Ranking & Candidate Matching System")

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)", accept_multiple_files=True
)

jd_input = st.text_area("Enter Job Description")

required_exp = st.number_input(
    "Required Experience (years)", min_value=0, value=1
)

if st.button("Process Resumes"):

    if uploaded_files and jd_input:

        with st.spinner("Processing resumes..."):

            resumes_data = parse_resumes(uploaded_files)

            
            results = rank_candidates(
                resumes_data,
                jd_input,
                required_exp
            )

            df = pd.DataFrame(results)

            
            df = df.sort_values(by="Score", ascending=False).reset_index(drop=True)
            df["Rank"] = df.index + 1

            
            df = df[["Rank", "Name", "Skills", "Experience", "Score"]]

            st.subheader("Ranked Candidates")
            st.dataframe(df, width='stretch')

    else:
        st.warning("Please upload resumes and enter job description.")