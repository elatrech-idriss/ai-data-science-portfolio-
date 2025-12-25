import streamlit as st

st.set_page_config(
    page_title="Idriss – AI Portfolio",
    page_icon="💡",
    layout="wide"
)

# ⚠️ CSS DOIT ÊTRE CHARGÉ ICI
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# CONTENU APRÈS
st.title("💡 Idriss – AI & Data Science Portfolio")
st.write("Bienvenue ! Utilise le menu à gauche pour naviguer dans mon portfolio.")
