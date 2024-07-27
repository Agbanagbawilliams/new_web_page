import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Multi App",
    page_icon="😁",
)

st.title("Homepage")
st.write("Hi i am Williams")
st.sidebar.success("Select a pages above.")

img_lottie_animation = ("images/download.png")
st.image(img_lottie_animation)
st.write("Welcome to my multi page")
st.write("""In this webpage you can 
 discover and see my work""")
st.success("Check in the sidebar for more apps!")

# ---- About me ----
st.title("About me")
st.write("I am a 9 years old boy who is learning how to code on programing languages")

# ---- GOALS ----
st.title("My Goals")

st.write("""My Goals are to
- To learn about python
- To make games in python
- learn how to use other stuff that goes with python like streamlit"""
         )

# ---- This webpage ----
st.title("About this webpage")

st.write("This webpage was made using python *A programing language*, streamlit *A faster way to build and share data apps*")

img_streamlit = ("images/streamlit.png")
st.image(img_streamlit)
img_python = ("images/python.jpg")
st.image(img_python)

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

st.logo("asset/logo.png")
st.sidebar.text("Created by 💖 Williams")
