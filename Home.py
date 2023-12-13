import streamlit as st
import base64
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Introduction to Machine Learning", page_icon=":shark:", layout="wide",)


st.title("Introduction to :rainbow[Machine Learning]")   

col1 , col2 = st.columns(2)
with col1:
    st_lottie("https://lottie.host/91531ae8-25f0-4816-a0b1-9e70cd032228/4Vdw4SYXyL.json", height=400)
with col2:
    st.markdown("#### Welcome to this introductory course on Machine Learning.",)
    st.write('''
             My name is :blue[Lee Bundi] and I am a **Data Scientist** who is passionate 
             about Machine Learning and Data Science.\n This Blog is designed to teach you all the basic knowledge of Machine Learning.
             ''',)



##################################### Page info ##############################################################################

st.sidebar.markdown("#### About")
st.sidebar.info(
    """
    Graduate : Masters in Data Science & Analytics.
    """
)

st.sidebar.markdown("#### :brown[Contact]")
st.sidebar.markdown(
    """<a href="https://github.com/NUELBUNDI/">
    <img src="data:image/png;base64,{}" width="25">
    </a>""".format(
        base64.b64encode(open("assets/github.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
