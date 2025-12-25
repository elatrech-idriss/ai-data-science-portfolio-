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
st.title("🧠 Machine Learning Projects")

st.write(
    "This page presents a selection of machine learning projects covering "
    "supervised and unsupervised learning, neural networks, and model evaluation. "
    "Each project includes a short description and a link to the full implementation on GitHub."
)

st.divider()

# -------------------------------------------------
# Projects data
# -------------------------------------------------
projects = [

    # -------------------------------------------------
    # Neural Networks (MLP)
    # -------------------------------------------------
    {
        "title": "Neural Networks for Regression and Classification",
        "description": (
            "This project explores the fundamental principles of neural networks "
            "and their application to regression, binary classification, and "
            "multiclass classification problems. It focuses on model architecture, "
            "training dynamics, and performance evaluation."
        ),
        "tech": "Python · NumPy · scikit-learn · Neural Networks (MLP)",
        "images": [
            "assets/images/machine_learning/MlpRegressor.png",
            "assets/images/machine_learning/MLPClassifier.png",
        ],
        "github": "https://github.com/elatrech-idriss/Neural-Networks-for-Regression-and-Classification"
    },

    # -------------------------------------------------
    # Customer Segmentation (K-Means)
    # -------------------------------------------------
    {
        "title": "Customer Segmentation with K-Means Clustering",
        "description": (
            "This project performs customer segmentation using K-Means clustering "
            "on demographic and spending data. Multiple clustering evaluation "
            "metrics are used to determine the optimal number of clusters. "
            "The resulting segments support marketing strategies and business decisions."
        ),
        "tech": (
            "Python · pandas · scikit-learn · K-Means · "
            "Unsupervised Learning · Clustering Metrics"
        ),
        "images": [
            "assets/images/machine_learning/distribution_dataset.png",
            "assets/images/machine_learning/metrics.png",
            "assets/images/machine_learning/Revenue_vs_Score_de_dépense.png",
        ],
        "github": "https://github.com/elatrech-idriss/customer-segmentation-clustering"
    },

    # -------------------------------------------------
    # Classical ML Models
    # -------------------------------------------------
    {
        "title": "Machine Learning Exploration: Decision Tree, KNN, and SVM",
        "description": (
            "This project explores classical machine learning algorithms including "
            "Decision Trees, K-Nearest Neighbors (KNN), and Support Vector Machines (SVM). "
            "It focuses on understanding overfitting and underfitting, comparing "
            "training and validation performance, and visualizing model behavior."
        ),
        "tech": (
            "Python · scikit-learn · Decision Trees · KNN · SVM · "
            "Bias–Variance Tradeoff"
        ),
        "images": [
            "assets/images/machine_learning/KNN_Regression-Train_vs_Validation.png",
            "assets/images/machine_learning/Effect_of_max_depth.png",
        ],
        "github": "https://github.com/elatrech-idriss/Machine-Learning-Exploration-Decision-Tree-KNN-SVM"
    },

    # -------------------------------------------------
    # Deep Learning – MNIST
    # -------------------------------------------------
    {
        "title": "MNIST Image Classification with Machine Learning and Deep Learning",
        "description": (
            "This project focuses on handwritten digit classification using the "
            "MNIST dataset. It compares traditional machine learning approaches "
            "(logistic regression / SGD) with deep learning models, including "
            "Multi-Layer Perceptrons (MLP) and Convolutional Neural Networks (CNN). "
            "The project analyzes training dynamics, model capacity, and test performance."
        ),
        "tech": (
            "Python · TensorFlow / Keras · Deep Learning · CNN · MLP · MNIST"
        ),
        "images": [
            "assets/images/machine_learning/Detection_nombre.png",
            "assets/images/machine_learning/FIC.png",
        ],
        "github": "https://github.com/elatrech-idriss/MNIST-Image-Classification-ML-and-Deep-Learning"
    }
]

# -------------------------------------------------
# Display projects
# -------------------------------------------------
for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
    st.caption(project["tech"])

    st.markdown("**Project visualizations:**")

    cols = st.columns(min(3, len(project["images"])))
    for col, img_path in zip(cols, project["images"]):
        with col:
            st.image(img_path, use_container_width=True)

    st.link_button("🔗 View full project on GitHub", project["github"])
    st.divider()
