import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Multi App",
    page_icon="😁",
)

st.title("Homepage")
st.write("Hi i am Williams")
st.sidebar.success("Select a pages above.")

st.write("Welcome to my multi page")
st.write("""In this webpage you can 
 discover and see my work""")
st.success("Check in the sidebar for more apps!")

st.title("About me")
st.write("I am a 10 years old boy who love to program in programing language")

# ---- GOALS ----
st.title("Goals")

st.write("""
- To learn about python
- To learn about streamlit
- To Learn python basic
- To learn about pygame
- To make awsome webpages
        """)

st.title("Hard Goals")
st.write("""
- To use other programing language
- To start making money
- And start using exel and powerpoint
""")


hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

st.logo("asset/logo.png")
st.sidebar.text("Created by 💖 Williams")