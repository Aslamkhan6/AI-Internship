from sklearn.feature_extraction.text import TfidfVectorizer


class FeatureExtractor:
    def __init__(self, text):
        self.text = text
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            min_df=1,
            sublinear_tf=True,
        )

    def fit_transform(self):
        self.text = self.vectorizer.fit_transform(self.text)
        return self.text

    def transform(self, text):
        return self.vectorizer.transform(text)