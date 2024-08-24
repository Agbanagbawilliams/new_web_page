import streamlit as st
import pandas as pd

st.title("📊Sales Dashboard")

st.subheader("Excel sheet")
def load_data(path: str):
    data = pd.read_excel(path)
    return data
upload_file = st.file_uploader("Chose a file")
if upload_file is None:

    df = load_data("Work.xlsx")
    st.dataframe(df)

st.write("---")
st.subheader("Bar Chart")

def Data(path: str):
    bar = pd.read_excel(path)
    return bar
i = load_data("Work.xlsx")
st.bar_chart(i)