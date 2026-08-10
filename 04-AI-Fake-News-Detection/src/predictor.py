import numpy as np

from src.preprocessor import Preprocessor
from src.feature_extraction import FeatureExtractor
from src.label_encoder import LabelEncoderClass
from src.train_model import TrainModel


class Predictor:

    def __init__(self):

        # Load saved objects
        self.model = TrainModel.loadModel()

        self.vectorizer = FeatureExtractor.loadVectorizer()

        self.encoder = LabelEncoderClass.loadEncoder()

    # ==========================================
    # Predict News
    # ==========================================

    def predict(self, article):

        # Preprocess
        processor = Preprocessor(article)

        clean_text = " ".join(
            processor.preprocess()
        )

        # Feature Extraction
        vector = self.vectorizer.transform(
            [clean_text]
        )

        # Prediction
        prediction = self.model.predict(vector)

        label = self.encoder.inverse_transform(
            prediction
        )[0]

        # Confidence Score
        confidence = None

        if hasattr(self.model, "predict_proba"):

            confidence = np.max(
                self.model.predict_proba(vector)
            ) * 100

        elif hasattr(self.model, "decision_function"):

            score = self.model.decision_function(vector)

            confidence = (
                1 / (1 + np.exp(-np.max(score)))
            ) * 100

        return {

            "prediction": label,

            "confidence": round(confidence, 2)

        }