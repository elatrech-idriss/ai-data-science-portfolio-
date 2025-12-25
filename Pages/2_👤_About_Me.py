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

st.title("👤 About Me")

st.write("""
My name is **Idriss Elatrech**, and I am a final-year engineering student at **ESIEA**, 
currently completing a **double degree in Artificial Intelligence for Business Transformation** 
at **SKEMA Business School**.

I am actively seeking a **6-month end-of-studies internship** starting in **2026**, 
in the fields of **Data Science**, **Machine Learning**, **Artificial Intelligence**, 
or **AI for Business Transformation**.

My profile sits at the intersection of **advanced Machine Learning**, **AI engineering**, 
and **business-oriented AI solutions**. My academic background combines strong technical 
foundations with a strategic understanding of how AI can create value, optimize processes, 
and support data-driven decision-making within organizations.

---

### 🔹 What I Do
- Design, train, and evaluate **Machine Learning and Deep Learning models**  
- Develop **AI-driven analytical tools** and backend systems in Python  
- Build **data pipelines and data architectures** (structured & unstructured data)  
- Work with **SQL, NoSQL, and graph databases** (MySQL, MongoDB, Neo4j)  
- Deploy applications using **Docker**, APIs, and modern software engineering practices  
- Apply AI to **real business use cases**: forecasting, optimization, automation, and decision support  

---

### 🔹 What Drives Me
I am particularly motivated by projects that bridge the gap between 
**technical performance and business impact**.

I enjoy transforming raw data and complex models into:
- **Actionable insights**
- **Reliable AI systems**
- **Concrete solutions** that support operational efficiency and strategic decision-making  

My approach always balances:
- **Technical excellence** (models, algorithms, architectures)  
- **Business relevance** (KPIs, value creation, decision-making)  

---

### 🔹 Career Objective
I am aiming for roles such as:
- **Data Scientist**
- **Machine Learning Engineer**
- **AI Engineer**
- **AI / Data Consultant**
- **AI for Business Transformation Consultant**
- **Technology & Digital Transformation Consultant**

with the long-term goal of contributing to impactful AI projects within innovative teams.

---

### 📩 Contact
- **Email:** elatrech-krati@et.esiea.fr  
- **LinkedIn:** https://www.linkedin.com/in/idrisselatrech/  
- **GitHub:** https://github.com/elatrech-idriss  
""")
