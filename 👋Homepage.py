import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Multi App",
    page_icon="😁",
)

st.title("Homepage")
st.write("Hi i am Williams")
st.sidebar.success("Select a pages above.")
Video = "https://www.youtube.com/watch?v=fWjsdhR3z3c"
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

st.sidebar.text("Created by 💖 Williams")

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