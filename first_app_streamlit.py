# import streamlit as st

# st.title("Hello Streamlit-er 👋")
# st.markdown(
#     """ 
#     This is a playground for you to try Streamlit and have fun. 

#     **There's :rainbow[so much] you can build!**
    
#     We prepared a few examples for you to get started. Just 
#     click on the buttons above and discover what you can do 
#     with Streamlit. 
#     """
# )

# if st.button("Send balloons!"):
#     st.balloons()

import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO


load_dotenv()


client = genai.Client()


st.title("First Image Generator")
user_prompt = st.text_input("What do you want to generate image for?")


if st.button("Generate Image"):
   if not user_prompt:
       st.warning("Please enter the prompt!")
   else:
       try:
           with st.spinner("Generating image..."):
               response = client.models.generate_content(
               model="gemini-2.0-flash-exp-image-generation",
               contents=user_prompt,
               config=types.GenerateContentConfig(
                   response_modalities=['Text', 'Image']
               )
           )
          
           st.subheader("Generated Image")
           for part in response.candidates[0].content.parts:
               if part.text is not None:
                   st.write(part.text)
               elif part.inline_data is not None:
                   image = Image.open(BytesIO((part.inline_data.data)))
                   st.image(image)
              
       except Exception as e:
           print(e)
           st.error("Error generating image")

