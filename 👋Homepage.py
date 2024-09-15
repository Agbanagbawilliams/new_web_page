import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Multi App",
    page_icon="😁",
)

# Nav bar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #00B4F0">
  <a class="navbar-brand" target="_blank">Mech</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
     <li class="nav-item active">
        <a class="nav-link" href="https://newwebpage-nr9d95duhpvvbdx6mqjedc.streamlit.app/" target="_blank">Home</a>
      <li class="nav-item">
        <a class="nav-link" href="https://blank-app-quobxypwoytpuhz3cchas6.streamlit.app/" target="_blank">Chatbot</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Start Homepage
st.title("Williams")
st.write("Hi i am Williams")
st.write("Welcome to my multi page")
st.write("---")
st.subheader("About me")
st.write("I am a 10 years old boy who love to program in programing language")
st.write("---")
# ---- GOALS ----
st.subheader("Goals")
st.write("""
- To learn about python
- To learn about streamlit
- To Learn python basic
- To learn about pygame
- To make awsome webpages
        """)
st.write("---")
st.subheader("Hard Goals")
st.write("""
- To use other programing language
- To start making money
- And start using exel and powerpoint
""")


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ----CONTACT ME ----
import streamlit as st  # pip install streamlit

st.header(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/agbanagbawilliams@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")