from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from src.config import VECTORIZER_FILE


class FeatureExtractor:

    def __init__(self, text=None):
        self.text = text
        self.vectorizer = vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2),
    max_features=5000,
    min_df=2,
    max_df=0.95,
    sublinear_tf=True
)

    # Train TF-IDF and convert text into vectors
    def fit_transform(self):
        

        self.text = self.vectorizer.fit_transform(self.text)

        return self.text

    # Convert new text using trained vectorizer
    def transform(self, text):

        return self.vectorizer.transform(text)

    # Save vectorizer
    def saveVectorizer(self):

        joblib.dump(self.vectorizer, VECTORIZER_FILE)

        print("Vectorizer saved successfully.")

    # Load vectorizer
    def loadVectorizer(self):

        self.vectorizer = joblib.load(VECTORIZER_FILE)

        return self.vectorizer