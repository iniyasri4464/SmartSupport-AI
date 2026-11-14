# SmartSupport AI – Intelligent Customer Support System

An NLP-powered customer support application that automatically classifies customer complaints into relevant categories and provides rule-based troubleshooting recommendations.

## Project Overview

SmartSupport AI uses Natural Language Processing (NLP) and Machine Learning to understand customer complaints, predict their categories, and suggest possible solutions.

The application helps organize customer support requests and reduces the need for manual complaint categorization.

## Key Features

- **Complaint Classification:** Automatically classifies complaints into five categories.
- **Text Processing:** Uses TF-IDF to convert text into numerical features.
- **Machine Learning:** Uses Logistic Regression for complaint classification.
- **Smart Recommendations:** Provides keyword-based solutions according to the predicted category.
- **Fallback Handling:** Requests more details or suggests contacting support when the prediction score is below the configured threshold.
- **Interactive Dashboard:** Displays complaint statistics and category distributions using Streamlit.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| Scikit-learn | Machine Learning and TF-IDF |
| Logistic Regression | Complaint classification |
| Streamlit | Interactive web application |
| Joblib | Saving and loading trained models |
| PyArrow | Parquet dataset processing |
| Langdetect | Language detection |

## Complaint Categories

The model predicts five categories:

1. Account
2. Billing
3. Network
4. Order
5. Technical

## System Architecture

```text
Customer Complaint
        |
        v
   Text Input
        |
        v
 TF-IDF Vectorizer
        |
        v
Logistic Regression
        |
        v
Predicted Category
        |
        v
 Prediction Score
        |
   +----+----+
   |         |
   v         v
Sufficient  Low Score
   |         |
   v         v
Rule-Based   Request More
Solution     Details / Support
   |         |
   +----+----+
        |
        v
   Streamlit UI
```
## Application Screenshots

### 1. SmartSupport AI – Home Page
<!-- Upload your application home page screenshot here -->

![SmartSupport AI Home Page](screenshots/home-page.png)

### 2. Complaint Classification
<!-- Upload a screenshot showing complaint input and predicted category here -->

![Complaint Classification](screenshots/complaint-classification.png)

### 3. Recommendation System
<!-- Upload a screenshot showing the predicted category and suggested solution here -->

![Smart Recommendations](screenshots/recommendations.png)

### 4. Dataset Dashboard
<!-- Upload your dashboard screenshot showing complaint statistics and category distribution here -->

![Dataset Dashboard](screenshots/dashboard.png)

### 5. Model Evaluation
<!-- Upload your model evaluation results or classification report here -->

![Model Evaluation](screenshots/model-evaluation.png)

## Machine Learning Workflow

1. Collected customer support datasets.
2. Inspected and cleaned the datasets.
3. Selected relevant complaint categories.
4. Normalized category labels.
5. Detected and filtered non-English records from the selected IT support data.
6. Combined the prepared datasets.
7. Checked duplicate records and class imbalance.
8. Split the data into training and testing sets.
9. Applied TF-IDF vectorization.
10. Trained a class-weighted Logistic Regression model.
11. Evaluated the model using classification metrics and stratified cross-validation.
12. Saved the trained model and vectorizer using Joblib.

## Model Evaluation

The final prepared dataset contained 20,619 records.

**Test-set accuracy:** 99.63%

**Four-fold cross-validation:**
- Mean accuracy: 99.55%
- Macro precision: 0.864
- Macro recall: 0.927
- Macro F1-score: 0.886

The model uses `class_weight="balanced"` to address class imbalance.

**Important evaluation note:** The dataset includes synthetic customer-support text and mapped category labels. The Network category has only four records, and repeated language patterns may inflate evaluation scores. These metrics should not be interpreted as guaranteed real-world performance.

## Project Structure

```text
SmartSupport_AI/
│
├── app/
│   └── app.py
│
├── dataset/
│   └── complaints.csv
│
├── models/
│   ├── complaint_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── predict.py
│   ├── recommendations.py
│   ├── evaluate_model.py
│   ├── evaluate_final_model.py
│   ├── cross_validation.py
│   ├── check_dataset.py
│   ├── check_duplicates.py
│   ├── check_imbalance.py
│   └── other dataset preparation and testing scripts
│
├── documentation/
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/iniyasri4464/SmartSupport-AI.git
cd SmartSupport-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Prepare the dashboard dataset

The full `final_complaints.csv` dataset is excluded from this public repository. Obtain the source datasets from their original providers, follow their licence and attribution requirements, and recreate the prepared dataset using the scripts in `src/`.

Place the resulting `final_complaints.csv` inside the `dataset/` folder before launching the dashboard.

### 6. Run the application

```bash
streamlit run app/app.py
```

Open the local URL displayed in the terminal.

## Dataset Information

The project uses customer-support text from:

- Bitext Customer Support dataset.
- IT Support Tickets dataset.

The repository currently includes a small original sample dataset (`complaints.csv`). Full source datasets and the combined final dataset are not included.

Please refer to the original dataset providers for their licence and attribution requirements.

## Future Enhancements

- Improve performance on underrepresented complaint categories.
- Explore advanced NLP models such as BERT.
- Add confidence calibration and validation-based threshold selection.
- Integrate a database for storing customer complaints.
- Implement live customer support and ticket tracking.
- Add multilingual complaint classification.

## Author

**Iniya Sri**

B.Tech – Artificial Intelligence and Data Science

GitHub: https://github.com/iniyasri4464

---

If you find this project interesting, feel free to explore the repository and share feedback!