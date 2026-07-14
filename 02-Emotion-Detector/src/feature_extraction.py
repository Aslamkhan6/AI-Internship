from sklearn.feature_extraction.text import TfidfVectorizer
import joblib


class FeatureExtractor:
    
    def __init__(self,text):
        self.text = text
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self):

       self.text = self.vectorizer.fit_transform(self.text)
       return self.text


