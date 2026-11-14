# SmartSupport AI – Intelligent Customer Support System

## Project Overview
SmartSupport AI is an NLP-based customer support system that automatically classifies customer complaints into relevant categories and provides suitable recommendations.

The application uses Machine Learning to understand complaint text and help customers receive faster initial support.

## Key Features
- Automatic complaint classification
- TF-IDF text vectorization
- Logistic Regression classification model
- Class imbalance handling using class weights
- Confidence-based fallback mechanism
- Category-specific recommendation system
- Interactive Streamlit web application
- Dataset analytics dashboard

## Technologies Used
- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **NLP:** TF-IDF Vectorizer
- **ML Algorithm:** Logistic Regression
- **Data Processing:** Pandas
- **Model Storage:** Joblib
- **Frontend:** Streamlit

## Complaint Categories
1. Account
2. Billing
3. Network
4. Order
5. Technical

## Project Workflow
1. Customer enters a complaint.
2. TF-IDF converts the complaint into numerical features.
3. Logistic Regression predicts the complaint category.
4. The application checks the maximum predicted class probability.
5. If the score meets the configured 70% threshold, a recommendation is displayed.
6. Otherwise, the application requests more details or suggests contacting customer support.

## Dataset Information
- Final dataset contains 20,619 records.
- Five complaint categories.
- Dataset combines Bitext customer support data, selected IT support ticket data, and a small initial sample.
- Data cleaning, duplicate removal, language filtering and category mapping were performed.

Note: Some category mappings are approximate. Dataset sources and their applicable licenses should be acknowledged when redistributing the project.

## Model Evaluation
- Algorithm: Logistic Regression
- Feature extraction: TF-IDF
- Class imbalance handling: `class_weight="balanced"`
- Cross-validation: 4-fold Stratified Cross-Validation
- Mean cross-validation accuracy: approximately 99.55%
- Mean macro F1-score: approximately 0.886

The dataset contains synthetic and templated examples, and the Network category has very few samples. Therefore, these evaluation results should not be interpreted as guaranteed real-world performance.

The 70% prediction-score threshold is an initial demonstration setting and is not a calibrated confidence measure.

## Project Structure
```text
SmartSupport_AI/
│
├── dataset/
├── models/
├── src/
├── app/
│   └── app.py
├── documentation/
├── requirements.txt
└── README.md
```

## Installation and Execution

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SmartSupport_AI
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the environment

Windows:
```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the application
```bash
streamlit run app/app.py
```

## Future Enhancements
- Improve classification of minority categories.
- Add more diverse real-world complaint examples.
- Improve recommendation accuracy.
- Evaluate and calibrate prediction thresholds.
- Add complaint history and human-agent escalation.

## Author
Developed as an AI and Machine Learning portfolio project.
