# 😊 Emotion Detector using Machine Learning

A Machine Learning based Emotion Detection System that predicts the emotion of a given text using Natural Language Processing (NLP).

This project preprocesses text, converts it into numerical features using **TF-IDF**, trains multiple machine learning models, compares their performance, and saves the best-performing model for future predictions.

---

## 🚀 Features

- Load emotion dataset
- Text preprocessing
- TF-IDF feature extraction
- Train multiple machine learning models
- Compare model performance
- Save the best trained model
- Ready for deployment with Streamlit

---

## 📂 Project Structure

```
02-Emotion-Detector/
│
├── dataset/
│   └── train.csv
│
├── model/
│   └── emotion_model.pkl
│
├── src/
│   ├── config.py
│   ├── datasets.py
│   ├── preproces.py
│   ├── feature_extraction.py
│   └── train_model.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📊 Dataset

Dataset: **Emotion Dataset**

Each row contains:

| Text | Emotion |
|------|----------|
| I am feeling happy | joy |
| I feel lonely | sadness |
| I am scared | fear |

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- NLTK
- Joblib
- Streamlit (Deployment)

---

## ⚙️ Project Workflow

```
Dataset
   │
   ▼
Load Dataset
   │
   ▼
Text Preprocessing
   │
   ▼
TF-IDF Feature Extraction
   │
   ▼
Train Machine Learning Models
   │
   ▼
Compare Accuracy
   │
   ▼
Save Best Model
```

---

## 🧹 Text Preprocessing

The preprocessing pipeline includes:

- Convert text to lowercase
- Remove punctuation
- Remove numbers
- Remove extra spaces
- Tokenization
- Remove stopwords
- Lemmatization

---

## 📈 Feature Extraction

The cleaned text is converted into numerical vectors using:

- **TF-IDF (Term Frequency-Inverse Document Frequency)**

---

## 🤖 Machine Learning Models

Three models were trained and evaluated.

| Model | Accuracy |
|--------|---------:|
| Multinomial Naive Bayes | 63.81% |
| Logistic Regression | 84.75% |
| Linear Support Vector Classifier (LinearSVC) | **90.13%** |

---

## 🏆 Best Model

The best-performing model was:

**Linear Support Vector Classifier (LinearSVC)**

Final Accuracy:

```
90.13%
```

This trained model is saved using **Joblib** for future emotion prediction.

---

## 💾 Saved Model

The trained model is stored in:

```
model/emotion_model.pkl
```

This model can later be loaded for real-time emotion prediction without retraining.

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/Aslamkhan6/AI-Internship.git
```

---

### Navigate to Project

```bash
cd 02-Emotion-Detector
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Train Model

```bash
python main.py
```

---

## 📌 Future Improvements

- Streamlit Web Application
- Real-time Emotion Prediction
- Deep Learning (LSTM/BERT)
- Model Hyperparameter Tuning
- REST API Integration

---

## 👨‍💻 Author

**Aslam Khan**

BS Computer Science Student

GitHub: https://github.com/Aslamkhan6

---

## 📄 License

This project was developed as part of an AI Internship for educational and learning purposes.