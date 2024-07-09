import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pypdf
from dotenv import load_dotenv
import json
import time


load_dotenv() ## load all our environment variables

genai.configure(api_key = os.getenv("GEMINI_PRO_API_KEY"))

def input_pdf_text(upload_file):
    pdfreader = pypdf.PdfReader(upload_file)
    text= ""
    for page in range(len(pdfreader.pages)):
        read = pdfreader.pages[page]
        #print(pdfreader.pages[page])
        text += read.extract_text()
    return text

def gemini_reponse(input):
    model= genai.GenerativeModel("gemini-pro")
    response= model.generate_content(input)
    return response.text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""


## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

# if submit:
#     if uploaded_file is not None:
#         text=input_pdf_text(uploaded_file)
#         response=gemini_reponse(input_prompt)
#         st.subheader(response)

if submit:
    if uploaded_file is not None:
        # Display the progress bar and the percentage
        progress_bar = st.progress(0)
        progress_text = st.empty()

        # Simulate an initial loading process (e.g., file reading)
        for percent_complete in range(50):
            time.sleep(0.05)  # Simulate time-consuming task
            progress_bar.progress(percent_complete + 1)
            progress_text.text(f"Loading... {percent_complete + 1}%")

        # Process the uploaded file
        text = input_pdf_text(uploaded_file)
        
        # Simulate additional loading while processing
        for percent_complete in range(50, 99):
            time.sleep(0.05)  # Simulate time-consuming task
            progress_bar.progress(percent_complete + 1)
            progress_text.text(f"Loading... {percent_complete + 1}%")
        
        # Get response from Gemini
        response = gemini_reponse(input_prompt)  # Assuming the function takes JD and resume text as input
        
        # Update to 100% once the response is received
        progress_bar.progress(100)
        progress_text.text("Loading... 100%")

        # Display the response
        st.subheader(response)
    