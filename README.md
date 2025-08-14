# CareerCraft-ATS-Optimized-Resume-Analyzer
CareerCraft is an intelligent web application designed to analyze resumes and provide ATS (Applicant Tracking System)-friendly feedback using Google’s Gemini AI. It helps job seekers improve their resumes by identifying missing keywords, offering personalized job-fit analysis
# Project Flow
User interacts with the UI to enter the input. 
User input is collected from the UI and transmitted to the backend using the Google API key.
The input is then forwarded to the Gemini Pro pre-trained model via an API call.
The Gemini Pro pre-trained model processes the input and generates the output.
The results are returned to the frontend for formatting and display.
# Project Structure
images folder: It is established to store the images utilized in the user interface.
.env file: It securely stores the Google API key.
app.py: It serves as the primary application file housing both the model and Streamlit UI code.
requirements.txt: It enumerates the libraries necessary for installation to ensure proper functioning.
# Create a requirements.txt file to list the required libraries.
streamlit: Streamlit is a powerful framework for building interactive web applications with Python.
streamlit_extras: Additional utilities and enhancements for Streamlit applications.
google-generativeai: Python client library for accessing the GenerativeAI API, facilitating interactions with pre-trained language models like Gemini Pro.
python-dotenv: Python-dotenv allows you to manage environment variables stored in a .env file for your Python projects.
PyPDF2: It is a Python library for extracting text and manipulating PDF documents.
Pillow: Pillow is a Python Imaging Library (PIL) fork that adds support for opening, manipulating, and saving many different image file formats.
# Generate and Initialize Google API Key
Link: https://ai.google.dev/gemini-api/docs/api-key . After signing in to your account, navigate to the 'Get an API Key' option.
Create a .env file and define a variable named GOOGLE_API_KEY. 
Assign the copied Google API key to this variable. 
Paste the API key obtained from the previous steps here.
# Load the Gemini Pro pre-trained model
The code begins by importing necessary libraries and modules, including dotenv, Streamlit, os, PyPDF2, GenerativeAIfrom Google, PIL (Python Imaging Library), and a custom module for adding vertical space in Streamlit.It loads environment variables from the .env file using the load_dotenv() function.
The GenerativeAI module is configured with the Google API key stored in the environment variable GOOGLE_API_KEY.
A GenerativeModel object named "model" is created using the Gemini Pro pre-trained model from Google.
The code is essentially setting up the environment, configuring the GenerativeAI module with the API key,and loading the Gemini Pro model for generating responses to user inputs in the Streamlit app.
# Implement a function to get gemini response
The function get_gemini_response takes an input text as a parameter.
It calls the generate_content method of the model object to generate a response.
The generated response is returned as text.
# Implement a function to read PDF content
The function input_pdf_text takes an uploaded PDF file as input.
It creates a PdfReader object from the PyPDF2 library to read the uploaded PDF file.
It initializes an empty string variable text to store the extracted text from the PDF.
It iterates over each page of the PDF using a loop.
For each page, it extracts the text using the extract_text() method and appends it to the text variable.
Finally, it returns the concatenated text extracted from all pages of the PDF
# Write a prompt for gemini model
The input_prompt is a multiline string containing instructions for an ATS (Applicant Tracking System).
It describes the expertise required for the ATS, including proficiency in various technical domains such as Software Engineering, Data Science, etc.
The objective of the ATS is to assess resumes against provided job descriptions in a competitive job market.
It requests the response to be structured into three sections: percentage match with the job description, a list of missing keywords, and a profile summary.
## Model Deployment
We deploy our model using the Streamlit framework, a powerful tool for building and sharing data applications quickly and easily. With Streamlit, we can create interactive web applications that allow users to interact with our models in real-time, providing an intuitive and seamless experience.
Integrate with Web Framework
The webpage is organized into four main sections to provide users with a comprehensive experience: 
## Introduction: 
!("C:\Users\kurup\OneDrive\Pictures\Screenshots\Screenshot (83).png")
The provided code sets the page configuration for a Streamlit application titled "Resume ATS Tracker" with a wide layout. 
It then creates a layout with two columns, where the first column is three times wider than the second. 
In the first column, it displays the title "CareerCraft" along with a header and a markdown text introducing CareerCraft as an ATS-Optimized Resume Analyzer. 
In the second column, it displays an image sourced from a URL, adjusting its width to fit the column. 
Overall, the code creates a visually appealing interface for the CareerCraft application, combining text and images to convey its features and benefits to users
## Offerings:
!("C:\Users\kurup\OneDrive\Pictures\Screenshots\Screenshot (87).png")
The provided code creates a two-column layout using Streamlit, with the first column containing an image and the second column containing a header followed by a list of offerings. 
The header "Wide Range of Offerings" introduces the list, which includes various features such as ATS-Optimized Resume Analysis, Resume Optimization, Skill Enhancement, and others. 
Overall, this layout effectively presents the range of services provided by the application in a clear and organized manner.
## Resume ATS Tracking Application:
!("C:\Users\kurup\OneDrive\Pictures\Screenshots\Screenshot (84).png")
This code snippet creates a two-column layout using Streamlit. 
In the left column (`col1`), it displays a header inviting users to embark on their career adventure, followed by a text area for pasting the job description and a file uploader for uploading the resume. 
Upon clicking the "Submit" button, it retrieves the text from the uploaded PDF resume, generates a response using the `get_gemini_response` function based on the provided job description, and displays the response as a subheader. 
In the right column (`col2`), it displays an image representing the career adventure concept. 
Overall, this layout allows users to interactively submit their job descriptions and resumes while visually engaging with the application's theme.
## FAQ:
!("C:\Users\kurup\OneDrive\Pictures\Screenshots\Screenshot (86).png")
This code snippet divides the page into two columns using Streamlit's `st.columns()` function. 
In the right column (`col2`), it displays a FAQ section with questions and answers about CareerCraft. 
Each question and answer pair is presented using `st.write()`. 
Additionally, vertical space is added between each question and answer pair using `avs.add_vertical_space()`. 
In the left column (`col1`), an image is displayed using `st.image()`. 
This layout effectively organizes the FAQ content alongside visual elements, enhancing the user experience.
## Host the Application
Launching the Application:
To host the application,  go to the terminal, type - streamlit run app.py
Here app.py refers to a python script.
 Here is the web application https://careercraft-ats-optimized-resume-analyzer-y3m64zctqgagfe9wfakf.streamlit.app/
<img src="images/images/Screenshot (83).png"/>
<img src="images/images/Screenshot (84).png"/>
<img src="images/images/Screenshot (85).png"/>
<img src="images/images/Screenshot (87).png"/>
<img src="images/images/Screenshot (86).png"/>


