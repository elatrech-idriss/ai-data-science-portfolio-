import streamlit as st

def load_css():
    with open("style.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()  # 🔥 OBLIGATOIRE

st.title("📂 Projects")

st.write(
    "Explore my work across different domains, including Machine Learning, "
    "AI for Business Transformation, and Software & Data Engineering."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🧠 Machine Learning")
    st.write("Supervised learning, neural networks, model evaluation, and predictive analytics.")
    st.page_link(
        "pages/5_Machine_Learning.py",
        label="View projects →",
        icon="🧠"
    )

with col2:
    st.markdown("### 💼 AI for Business Transformation")
    st.write("AI-driven decision support, forecasting, and optimization for business use cases.")
    st.page_link(
        "pages/6_AI_for_Business.py",
        label="View projects →",
        icon="💼"
    )

with col3:
    st.markdown("### ⚙️ Software & Data Engineering")
    st.write("Backend development, APIs, data pipelines, and engineering workflows.")
    st.page_link(
        "pages/7_Engineering.py",
        label="View projects →",
        icon="⚙️"
    )
