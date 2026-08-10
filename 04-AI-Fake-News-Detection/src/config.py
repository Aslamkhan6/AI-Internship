import os

# ==========================================
# Base Directory
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==========================================
# Dataset Paths
# ==========================================

DATASET_FOLDER = os.path.join(BASE_DIR, "dataset")

FAKE_DATASET = os.path.join(DATASET_FOLDER, "Fake.csv")

TRUE_DATASET = os.path.join(DATASET_FOLDER, "True.csv")

# ==========================================
# Models Folder
# ==========================================

MODEL_FOLDER = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_FOLDER, exist_ok=True)

# ==========================================
# Saved Files
# ==========================================

MODEL_FILE = os.path.join(
    MODEL_FOLDER,
    "fake_news_model.pkl"
)

VECTORIZER_FILE = os.path.join(
    MODEL_FOLDER,
    "vectorizer.pkl"
)

ENCODER_FILE = os.path.join(
    MODEL_FOLDER,
    "label_encoder.pkl"
)