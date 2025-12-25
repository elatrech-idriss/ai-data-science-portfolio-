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


st.title("📞 Contact")

st.write("""
If you would like to get in touch, feel free to reach out using the information below.
""")

st.subheader("📧 Email")
st.write("elatrech-krati@et.esiea;fr")

st.subheader("🔗 LinkedIn")
st.write("https://www.linkedin.com/in/idrisselatrech/")

st.subheader("🐙 GitHub")
st.write("https://github.com/elatrech-idriss")
