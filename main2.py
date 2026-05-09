##import streamlit as st
from google import genai
import streamlit as st
st.title("AI Business idea Validation for Start Up")

prime = genai.Client(api_key = "AIzaSyAW4kVv2JydveDoxcNb9RQ6D8lkgn3dvIE")

audience = st.text_input ("Who are your audience")
age_group = st.text_input("Which are your age group")
country = st.text_input("which country you are targeting")
idea = st.text_input("Give your business idea")

prompt = f"""
You are a business strategist and marketing expert.

Based on the following details:
- Audience: {audience}
- Age Group: {age_group}
- Target Country: {country}
- Business Idea: {idea}

Please provide:
1. A clear business overview
2. Target customer pain points
3. Unique selling proposition (USP)
4. Best marketing channels
5. Social media content ideas
6. Revenue model suggestions
7. Competitor analysis overview
8. Step-by-step launch plan
9. Potential challenges and solutions
10. Growth strategy for scaling

Make the response practical, modern, and tailored to the target country and audience.
"""


##st.title("My Own GPT")
##st.header("This is my personal GPT")

##question = st.text_input("Ask Anything")
##pressed = st.button("submit")
##if question or pressed :
if st.button("Generate Report"):
    with st.spinner("Generating Report"):
        response = prime.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
            )
        st.write(response.text)
#print(response.text)