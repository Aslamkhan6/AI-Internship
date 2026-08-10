import joblib

from sklearn.feature_extraction.text import TfidfVectorizer

from src.config import VECTORIZER_FILE


class FeatureExtractor:

    def __init__(self, text):

        self.text = text

        self.vectorizer = TfidfVectorizer(

            lowercase=False,

            max_features=5000,

            stop_words=None,

            ngram_range=(1, 2),

            min_df=2,

            max_df=0.95

        )

    # ==========================================
    # Train TF-IDF
    # ==========================================

    def fit_transform(self):

        self.text = self.vectorizer.fit_transform(self.text)

        return self.text

    # ==========================================
    # Transform New Data
    # ==========================================

    def transform(self, text):

        return self.vectorizer.transform(text)

    # ==========================================
    # Save Vectorizer
    # ==========================================

    def saveVectorizer(self):

        joblib.dump(

            self.vectorizer,

            VECTORIZER_FILE

        )

        print("Vectorizer Saved Successfully.")

    # ==========================================
    # Load Vectorizer
    # ==========================================

    @staticmethod
    def loadVectorizer():

        return joblib.load(VECTORIZER_FILE)