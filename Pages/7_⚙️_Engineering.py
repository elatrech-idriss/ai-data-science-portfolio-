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
st.title("⚙️ Software & Engineering Projects")

st.write(
    "This section highlights software engineering projects focused on "
    "automation, backend development, tooling, and AI-assisted systems. "
    "These projects emphasize code quality, system design, and real-world "
    "engineering constraints."
)

st.divider()

# -------------------------------------------------
# Engineering projects
# -------------------------------------------------
projects = [
    {
        "title": "LLM-Powered Code Reviewer",
        "description": (
            "This project is a **Python-based automated code review system** designed "
            "to evaluate **Java projects** using the reasoning capabilities of "
            "**Large Language Models (LLMs)**.\n\n"
            "The system analyzes source code, structured evaluation questions, and "
            "project constraints to generate **detailed, pedagogical feedback**, "
            "including strengths, weaknesses, and concrete improvement suggestions.\n\n"
            "It is particularly suited for **automated grading**, **educational platforms**, "
            "and **software quality assessment pipelines**."
        ),
        "tech": (
            "Python · Large Language Models (LLMs) · Software Engineering · "
            "Code Analysis · Automation · Java Evaluation"
        ),
        "image": "assets/images/Engineering/reponse111.png",
        "github": "https://github.com/elatrech-idriss/LLM-Powered-Code-Reviewer"
    }
]

# -------------------------------------------------
# Display projects
# -------------------------------------------------
for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
    st.caption(project["tech"])

    # Display result image
    st.image(
        project["image"],
        caption="Example of automated LLM-generated code review feedback",
        use_container_width=True
    )

    st.markdown(f"🔗 **[View project on GitHub]({project['github']})**")
    st.divider()
