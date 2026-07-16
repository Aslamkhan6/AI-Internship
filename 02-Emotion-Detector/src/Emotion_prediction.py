import joblib
from src.preproces import Preprocessor


class EmotionPredictor:
    def __init__(self, model_path, vectorizer_path):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def predict_emottion(self, text):
        process = Preprocessor(text)
        clean_text = process.preprocess()
        clean_text = " ".join(clean_text)

        vector = self.vectorizer.transform([clean_text])
        emotion = self.model.predict(vector)
        return emotion[0]


       
