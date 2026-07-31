import os

# ==============================
# Project Root Directory
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==============================
# Dataset Paths
# ==============================

DATASET_DIR = os.path.join(BASE_DIR, "dataset")

DATASET_FILE = os.path.join(DATASET_DIR, "intents.json")

# ==============================
# Model Paths
# ==============================

MODEL_DIR = os.path.join(BASE_DIR, "model")

MODEL_FILE = os.path.join(MODEL_DIR, "chatbot_model.pkl")

VECTORIZER_FILE = os.path.join(MODEL_DIR, "vectorizer.pkl")

LABEL_ENCODER_FILE = os.path.join(MODEL_DIR, "label_encoder.pkl")

# ==============================
# Ensure Required Directories Exist
# ==============================

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(DATASET_DIR, exist_ok=True)