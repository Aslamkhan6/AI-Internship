import os

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Folder paths
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
MODELS_DIR = os.path.join(BASE_DIR, "model")
TRAINER_DIR = os.path.join(BASE_DIR, "trainer")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Model file
HAAR_CASCADE_PATH = os.path.join(
    MODELS_DIR,
    "haarcascade_frontalface_default.xml"
)


# Dataset Settings
IMAGE_SIZE = (200, 200)
IMAGES_PER_PERSON = 50

# Labels File
MODEL_FILE = os.path.join(
    TRAINER_DIR,
    "trainer.yml"
)

LABELS_FILE = os.path.join(
    TRAINER_DIR,
    "labels.json"
)

# Create folders if they don't exist
for folder in [DATASET_DIR, TRAINER_DIR, OUTPUT_DIR]:
    os.makedirs(folder, exist_ok=True)