import streamlit as st
from PIL import Image

st.title("Payment💰")

# --- Buy stuff with money ---
st.write("Click here to buy")
st.write("https://buy.stripe.com/test_cN215l5qb13B2aY8wz")
img_lottie_animation = Image.open("images/coffe.jpg")
st.image(img_lottie_animation)
st.write("Click here to buy")
st.write("https://buy.stripe.com/test_28o15l05RfYvaHu4gk")
img_photo = Image.open("images/download.jpg")
st.image(img_photo)

# ---- HIDING THE STREAMLIT LOGO ----
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# ---- ADDING THE LOGO ----
st.markdown(hide_st_style, unsafe_allow_html=True)

st.logo("asset/logo.png")
st.sidebar.text("Created by 💖 Williams")