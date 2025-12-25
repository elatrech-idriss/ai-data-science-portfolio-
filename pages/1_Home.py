import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Idriss – AI Portfolio",
    page_icon="💡",
    layout="wide"
)

load_css()  # 🔥 OBLIGATOIRE

st.title("🏠 Welcome to my AI & Data Science Portfolio")

st.write("""
Welcome to my portfolio dedicated to Artificial Intelligence, Data Science, 
AI for Business Transformation.

Here you will find a selection of projects showcasing my expertise in:
- Machine Learning & Deep Learning  
- Data analysis, modeling, and predictive analytics  
- Applied Artificial Intelligence for real business use cases  
- AI for Business Transformation (decision-making, optimization, automation)  
- Python development & backend engineering  
- Big Data & Data Engineering architectures  

This portfolio reflects my technical skills as well as my ability to design 
complete, reliable, and business-oriented AI solutions.
""")

st.write("Use the left-side menu to navigate through the different sections.")
