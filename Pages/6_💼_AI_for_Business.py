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


# -------------------------------------------------
# Page title & introduction
# -------------------------------------------------
st.title("💼 AI for Business Projects")

st.write(
    "This section presents applied AI projects focused on **business impact**, "
    "decision support, and large-scale system design. These projects emphasize "
    "architecture, data pipelines, and AI-driven optimization rather than "
    "standalone algorithms."
)

st.divider()

# -------------------------------------------------
# Projects data
# -------------------------------------------------
projects = [
    {
        "title": "GreenFlow – AI-Based Renewable Energy Management System",
        "description": (
            "GreenFlow is an AI-driven renewable energy management system developed "
            "in collaboration with **ENGIE**. The project focuses on optimizing "
            "energy production, storage, and distribution using artificial intelligence "
            "to support strategic decision-making in energy systems.\n\n"
            "The system combines predictive analytics, optimization logic, and "
            "data architecture design to improve efficiency, sustainability, and "
            "operational performance in renewable energy infrastructures."
        ),
        "tech": (
            "AI for Business · Energy Systems · Decision Support · "
            "Predictive Analytics · Optimization · Data Architecture"
        ),
        "images": [
            "assets/images/ai_for_business/image111.png",
            "assets/images/ai_for_business/image222.png",
        ],
        "github": "https://github.com/elatrech-idriss/GreenFlow-AI-Based-Renewable-Energy-Management-System"
    }
]

# -------------------------------------------------
# Display projects
# -------------------------------------------------
for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
    st.caption(project["tech"])

    cols = st.columns(len(project["images"]))
    for col, img_path in zip(cols, project["images"]):
        with col:
            st.image(img_path, use_container_width=True)

    st.markdown(f"📄 **[View project on GitHub]({project['github']})**")
    st.divider()
