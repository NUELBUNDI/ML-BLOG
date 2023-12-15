import streamlit as st
import base64
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Introduction to Machine Learning", page_icon=":shark:", layout="wide",)


# st.title("Introduction to :rainbow[Machine Learning]") 
st.markdown("<h1 style='text-align: center; color: #F3722C;'>Introduction to Applied Machine Learning</h1>", unsafe_allow_html=True)
st.divider()
col1 , col2 = st.columns(2)
with col1:
    st_lottie("https://lottie.host/91531ae8-25f0-4816-a0b1-9e70cd032228/4Vdw4SYXyL.json", height=400)
with col2:
    st.subheader("Welcome!!🤗 to the world of Machine Learning with Lee ")
    st.write(" ")
    st.markdown('''
             Hello everyone ! 👋 My name is :blue[Lee Bundi] I am thrilled to embark on this journey with you.
             
             As a dedicated Data Scientist, my passion lies in unraveling the complexities of data and building models that can help us make better decisions.
             
             Through this blog, I aim to share my knowledge and experience with you.
             ''',)
    
    st.subheader("What You'll Learn Here")
    
    st.markdown('''
                
                1. :blue[**Fundametals of Machine Learning**] : Understand the basic types of Machine Learning, Supervised and Unsupervised Learning, 
                 and reinforcement learning.
                
                2. :blue[**Data Science Techniques**] : Data Preprocessing, Feature Engineering, Feature Selection, Model Selection, Model Evaluation,
                Model Validation, and Model Interpretation.
                
                3. :blue[**Machine Learning Algorithms**] :  Used in Supervised Learning, Unsupervised Learning
                
                4. :blue[**Real-world Applications**] :  Discover how Machine Learning can be applied to real-world problems.
                
                5. :blue[**Hands-on Projects**] :  Engage in practical projects to apply the concepts learnt in this blog. 
                
                ''')

st.info(        
    """ 
   Select the pages on sidebar  👈left  to start. Let's Begin Our Journey., 
    """)


# col_prereq, col_benefits = st.columns(2)

# with col_prereq:
#     st.subheader("Prerequisites")
    
#     st.markdown('''
#                 - Basic Programming Knowledge  especially Python is Key.
                
#                 - Basic Understanding of Statistics and Mathematics
                
#                 - Data Handling and Visualization with Python
                
#                 - Curiosity and a willingness to learn
                 
#                 ''')





##################################### Page info ##############################################################################

st.sidebar.markdown("#### About Me")
st.sidebar.info(
    """
    Msc Data Science & Analytics.\n
    Degree in Mathematics \n 
    Certified Public Accountant (CPAK)
    """
)

st.sidebar.markdown("#### :brown[Social Media]")

st.sidebar.markdown(
    """<a href="https://github.com/NUELBUNDI/">
    <img src="data:image/png;base64,{}" width="25">
    </a>""".format(
        base64.b64encode(open("assets/github.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)
st.sidebar.write(" ")
  
st.sidebar.markdown(
    """<a href="https://www.linkedin.com/in/lee-emmanuel-24055a116/">
    <img src="data:image/png;base64,{}" width="25">
    </a> """.format(
        base64.b64encode(open("assets/linkedin.png", "rb").read()).decode()
    ),
    unsafe_allow_html=True,
)


