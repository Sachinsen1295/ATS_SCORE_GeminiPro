# Smart ATS

This is a Streamlit application designed to improve resumes by evaluating them against job descriptions using an AI-powered ATS (Application Tracking System). The application extracts text from uploaded PDF resumes, sends the text along with the job description to a Generative AI model, and provides feedback to the user.

## Features

- Upload a resume in PDF format.
- Paste a job description.
- Get an evaluation of the resume based on the job description, including a JD match percentage, missing keywords, and a profile summary.
- Visual feedback with a progress bar showing the loading percentage.

## Setup

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Google Generative AI (`google-generativeai`)
- PyPDF2
- python-dotenv

### Installation

1. Clone this repository or download the code.

2. Install the required packages using pip:

    ```sh
    pip install streamlit google-generativeai PyPDF2 python-dotenv
    ```

3. Create a `.env` file in the root directory and add your Gemini API key:

    ```env
    GEMINI_PRO_API_KEY=your_api_key_here
    ```

## Usage

1. Run the Streamlit application:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Paste the job description in the provided text area.

4. Upload your resume in PDF format.

5. Click the `Submit` button.

6. The application will show a progress bar indicating the loading percentage. Once the process is complete, it will display the evaluation results.

## Code Explanation

### Importing Libraries

```python
import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pypdf
from dotenv import load_dotenv
import json
import time
