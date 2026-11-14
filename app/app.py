
import streamlit as st
import pandas as pd
import joblib
import sys
from pathlib import Path

# Project folder path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))

from recommendations import get_solution

# Load model and vectorizer
model = joblib.load(
    BASE_DIR / "models" / "complaint_model.pkl"
)

vectorizer = joblib.load(
    BASE_DIR / "models" / "tfidf_vectorizer.pkl"
)

# Load final dataset
df = pd.read_csv(
    BASE_DIR / "dataset" / "final_complaints.csv"
)

# Page configuration
st.set_page_config(
    page_title="SmartSupport AI",
    page_icon="🤖",
    layout="wide"
)

# Application title
st.title("🤖 SmartSupport AI")
st.subheader("Intelligent Customer Support System")

st.write(
    "An NLP-based system that classifies customer complaints "
    "and recommends suitable solutions."
)

# Navigation
page = st.sidebar.radio(
    "Choose Section",
    ["Complaint Analyzer", "Dataset Dashboard"]
)

# --------------------------------
# PAGE 1: COMPLAINT ANALYZER
# --------------------------------

if page == "Complaint Analyzer":

    st.header("Customer Complaint Analyzer")

    complaint = st.text_area(
        "Enter your complaint:",
        placeholder="Example: My internet connection is very slow"
    )

    if st.button("Analyze Complaint"):

        if complaint.strip():

            # Convert complaint into TF-IDF features
            complaint_tfidf = vectorizer.transform([complaint])

            # Predict category
            prediction = model.predict(complaint_tfidf)[0]

            # Calculate prediction score
            probabilities = model.predict_proba(
                complaint_tfidf
            )[0]

            confidence = max(probabilities) * 100
            st.write("Predicted Category:", prediction)

            st.subheader("Analysis Results")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Prediction Score",
                    f"{confidence:.2f}%"
                )

            with col2:
                st.metric(
                    "Analysis Status",
                    "Completed"
                )

            # Confidence-based recommendation
            if confidence >= 70:

                solution = get_solution(prediction, complaint)

                st.success("Complaint Analyzed Successfully!")

                st.metric(
                    "Predicted Category",
                    prediction
                )

                st.subheader("Recommended Solution")
                st.info(solution)

            else:

                st.warning(
                    "The system is not sufficiently confident "
                    "about this complaint."
                )

                st.write(
                    "Please provide more details or contact "
                    "customer support for assistance."
                )

        else:
            st.warning("Please enter a complaint.")

# --------------------------------
# PAGE 2: DATASET DASHBOARD
# --------------------------------


elif page == "Dataset Dashboard":

    st.header("📊 Dataset Analytics Dashboard")

    # Dataset statistics
    total_complaints = len(df)
    total_categories = df["category"].nunique()
    most_common_category = df["category"].value_counts().idxmax()

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Complaints", f"{total_complaints:,}")

    with col2:
        st.metric("Total Categories", total_categories)

    with col3:
        st.metric("Most Common Category", most_common_category)

    st.divider()

    # Category distribution
    st.subheader("Category-wise Complaint Distribution")

    category_counts = df["category"].value_counts()

    st.bar_chart(category_counts)

    st.divider()

    # Percentage distribution
    st.subheader("Category Percentage Distribution")

    percentage = (
        df["category"].value_counts(normalize=True) * 100
    ).round(2)

    percentage_df = pd.DataFrame({
        "Category": percentage.index,
        "Percentage": percentage.values
    })

    st.dataframe(
        percentage_df,
        width="stretch",
        hide_index=True
    )

    st.divider()

    # Dataset preview
    st.subheader("Dataset Preview")

    st.write("Showing the first 20 complaint records.")

    st.dataframe(
        df.head(20),
        width="stretch"
    )
    