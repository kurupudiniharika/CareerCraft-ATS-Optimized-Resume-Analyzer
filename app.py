from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai
import os
import PyPDF2
from PIL import Image
# Add background color
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #FAF3E0;
            color: #222222; /* Set your desired font color */
        }
        h1, h2, h3, h4, h5, h6, p, div {
            color: #222222 !important; /* Force font color for headings and text */
        }
    </style>
    """,
    unsafe_allow_html=True
)
)
# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

# Prompt template
input_prompt = """
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing
Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App 
Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, 
Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX 
Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess 
resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial 
in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the JD 
(Job Description) and meticulously identify any missing keywords with utmost accuracy.
resume:{text}
description:{jd}

I want the response in the following structure:
The first line indicates the percentage match with the job description (JD).
The second line presents a list of missing keywords.
The third section provides a profile summary.

Mention the title for all the three sections.
While generating the response put some space to separate all the three sections.
"""

# Streamlit page settings
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")
avs.add_vertical_space(4)

# Header section
col1, col2 = st.columns([3, 2])
with col1:
    st.title("CareerCraft")
    st.header("Navigate the Job Market with Confidence!")
    st.markdown("""
        <p style='text-align: justify;'>
        Introducing CareerCraft, an ATS-Optimized Resume Analyzer — your ultimate solution for optimizing 
        job applications and accelerating career growth. Our innovative platform leverages advanced ATS 
        technology to provide job seekers with valuable insights into their resumes' compatibility with 
        job descriptions. From resume optimization and skill enhancement to career progression guidance, 
        CareerCraft empowers users to stand out in today's competitive job market. Streamline your job 
        application process, enhance your skills, and navigate your career path with confidence. Join 
        CareerCraft today and unlock new opportunities for professional success!
        </p>
    """, unsafe_allow_html=True)

with col2:
    st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_container_width=True)

avs.add_vertical_space(10)

# Features section
col1, col2 = st.columns([3, 2])
with col2:
    st.header("Wide Range of Offerings")
    st.write('✔️ ATS-Optimized Resume Analysis')
    st.write('✔️ Resume Optimization')
    st.write('✔️ Skill Enhancement')
    st.write('✔️ Career Progression Guidance')
    st.write('✔️ Tailored Profile Summaries')
    st.write('✔️ Streamlined Application Process')
    st.write('✔️ Personalized Recommendations')
    st.write('✔️ Efficient Career Navigation')

with col1:
    img1 = Image.open("images/career image 1.png")
    st.image(img1, use_container_width=True)

avs.add_vertical_space(10)

# Main input section
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("📄 Paste the Job Description")
    uploaded_file = st.file_uploader("📎 Upload Your Resume (PDF only)", type="pdf")

    submit = st.button("🔍 Submit")

    if submit:
        if uploaded_file is not None and jd:
            text = input_pdf_text(uploaded_file)
            prompt = input_prompt.replace("{text}", text).replace("{jd}", jd)
            response = get_gemini_response(prompt)
            st.subheader(response)
        else:
            st.warning("⚠️ Please upload a resume and enter a job description.")

with col2:
    img2 = Image.open("images/career image 2.png")
    st.image(img2, use_container_width=True)

avs.add_vertical_space(10)

# FAQ section
col1, col2 = st.columns([2, 3])
with col2:
    st.markdown("<h1 style='text-align: center;'>❓ FAQ</h1>", unsafe_allow_html=True)

    st.write("**Q: How does CareerCraft analyze resumes and job descriptions?**")
    st.write("A: CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility.")

    avs.add_vertical_space(2)

    st.write("**Q: Can CareerCraft suggest improvements for my resume?**")
    st.write("A: Yes, CareerCraft provides personalized recommendations including suggestions for missing keywords and alignment with job roles.")

    avs.add_vertical_space(2)

    st.write("**Q: Is CareerCraft suitable for both entry-level and experienced professionals?**")
    st.write("A: Absolutely! It offers tailored insights and guidance for all career levels.")

with col1:
    img3 = Image.open("images/career image 3 - Copy.png")
    st.image(img3, use_container_width=True)

