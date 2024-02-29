import streamlit as st
import os
from PIL import Image
from gtts import gTTS
import os
st.set_page_config(page_title="Text To speech")
st.header("TTS app")
input=st.text_input("Input text: ",key="input")
submit=st.button("Speak out loud")
if submit:
    language = 'en'
    myobj = gTTS(text=input, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    st.audio('welcome.mp3')
