import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Multi App",
    page_icon="😁",
)

# Nav bar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# Nav bar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" target="_blank">Multi app</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="">href="https://newwebpage-nr9d95duhpvvbdx6mqjedc.streamlit.app/" Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://newwebpage-nr9d95duhpvvbdx6mqjedc.streamlit.app/Project" target="_blank">Project</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://blank-app-quobxypwoytpuhz3cchas6.streamlit.app/" target="_blank">Chatbot</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Start Homepage
st.title("Homepage")
st.write("Hi i am Williams")
st.write("Welcome to my multi page")
st.write("""In this webpage you can 
 discover, Buy and see my work""")
st.success("Check in the sidebar for more apps!")
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
st.write("---")
st.header("Contact Me📬")

st.text_input("First Name")
st.text_input("Last Name")
number = st.slider("Age", min_value=0, max_value=100)
st.text_input("Email")
st.text_input("Message")
submit_button = st.button("Submit")
if submit_button:
    st.success("Message successfully sent")
