# 🤖 AI Customer Support Chatbot

An AI-powered Customer Support Chatbot built with **Python**, **Scikit-learn**, and **Streamlit**. The chatbot uses **Natural Language Processing (NLP)** and **Machine Learning** to classify user intents and provide appropriate responses. It also includes a custom dataset generation pipeline capable of creating large-scale training datasets automatically.

---

# 📌 Features

* Intelligent intent classification
* Automatic response generation
* Custom NLP preprocessing pipeline
* TF-IDF feature extraction
* Multiple Machine Learning model comparison
* Automatic best model selection
* Streamlit web interface
* Large-scale dataset generation
* Modular and scalable project structure
* Model persistence using Joblib

---

# 🛠 Tech Stack

* Python 3.11+
* Scikit-learn
* NLTK
* Streamlit
* Joblib
* JSON

---

# 📂 Project Structure

```text
03-AI-Customer-Chatbot/

│── app.py
│── main.py
│── requirements.txt
│── README.md

│── dataset/
│     ├── generator.py
│     ├── templates.py
│     ├── synonyms.py
│     ├── grammar.py
│     ├── typo_generator.py
│     ├── responses.py
│     └── intents.json

│── models/
│     ├── chatbot_model.pkl
│     ├── vectorizer.pkl
│     └── label_encoder.pkl

│── src/
│     ├── config.py
│     ├── data_loader.py
│     ├── preproces.py
│     ├── feature_extraction.py
│     ├── label_encoder.py
│     ├── train_model.py
│     ├── predictor.py
│     └── chatbot.py

│── assets/
│── output/
```

---

# 🧠 Machine Learning Pipeline

```
Dataset
     │
     ▼
Data Loader
     │
     ▼
Text Preprocessing
     │
     ▼
TF-IDF Feature Extraction
     │
     ▼
Label Encoding
     │
     ▼
Train/Test Split
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Best Model Selection
     │
     ▼
Save Model + Vectorizer + Label Encoder
     │
     ▼
Streamlit Chatbot
```

---

# 📝 NLP Preprocessing

The chatbot performs several preprocessing steps before training:

* Convert text to lowercase
* Remove punctuation
* Remove numbers
* Remove extra spaces
* Tokenization
* Stopword removal
* Lemmatization

---

# 📊 Feature Extraction

The project uses **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert text into numerical vectors suitable for machine learning algorithms.

---

# 🤖 Machine Learning Models

The following models are trained and evaluated automatically:

* Multinomial Naive Bayes
* Logistic Regression
* Linear Support Vector Classifier (LinearSVC)

The model with the highest accuracy is automatically selected and saved.

---

# 💾 Saved Files

After training, the following files are generated:

* `chatbot_model.pkl`
* `vectorizer.pkl`
* `label_encoder.pkl`

These files are used during prediction without retraining the model.

---

# ⚙ Dataset Generator

Instead of manually writing thousands of patterns, the project includes an automated dataset generator.

### It supports:

* Template-based sentence generation
* Synonym replacement
* Grammar variation generation
* Typo generation
* Duplicate removal
* Automatic `intents.json` generation

The generator can produce **200,000+ training patterns** from a small number of templates.

---

# 💬 Supported Intent Categories

Example supported intents include:

* Greeting
* Goodbye
* Thanks
* Refund
* Order Status
* Shipping Information
* Payment Methods
* Account Management
* Product Inquiry
* Billing Issues
* Warranty
* Store Locations
* Complaints
* Security & Privacy
* Membership
* Exchanges
* Damaged Products
* Working Hours
* Weather
* News
* Songs
* Jokes
* Riddles
* Identity
* Programmer Information
* Date & Time
* And more...

---

# 🚀 How to Run

## 1. Clone the repository

```bash
git clone <repository-url>
cd 03-AI-Customer-Chatbot
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Generate the dataset

```bash
python dataset/generator.py
```

---

## 5. Train the chatbot

```bash
python main.py
```

---

## 6. Launch the application

```bash
streamlit run app.py
```

---

# 📈 Future Improvements

Planned enhancements include:

* Entity Recognition
* Intent Balancing
* Data Augmentation
* Context-Aware Conversations
* Multi-turn Dialogue
* Voice Input
* Text-to-Speech
* Chat History
* Authentication
* REST API
* Database Integration
* Admin Dashboard
* Docker Support
* Cloud Deployment
* Analytics Dashboard
* Continuous Model Retraining

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Natural Language Processing
* Text Classification
* Machine Learning
* Feature Engineering
* Dataset Generation
* Python Development
* Scikit-learn
* Streamlit
* Software Architecture
* Model Deployment

---

# 📄 License

This project is created for educational and portfolio purposes.

---

# 👨‍💻 Author

**Aslam Khan**

BS Computer Science Student

Python • Machine Learning • NLP • MERN Stack

