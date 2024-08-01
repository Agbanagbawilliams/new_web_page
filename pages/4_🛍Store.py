import streamlit as st
from PIL import Image

st.set_page_config(page_title="Store", page_icon="🛍")

st.title("Store")

st.write("---")
st.title("PS5")
PS5 = ("images/download.jpg")
st.image(PS5)
st.link_button("Buy",
                   "https://buy.stripe.com/test_5kAdS79GrbIfaHu005")

st.write("---")
st.title("Coffe")
Coffe = ("images/coffe.jpg")
st.image(Coffe)
st.link_button("Buy",
                   "https://buy.stripe.com/test_cN215l5qb13B2aY8wz")

st.write("---")
st.title("Renzor Knockdown")
Knock = ("images/download (6).jpg")
st.image(Knock)
st.link_button("Buy",
                   "https://buy.stripe.com/test_aEU15l2dZ9A79DqfZ6")

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

st.logo("asset/logo.png")
st.sidebar.text("Created by 💖 Williams")