from src.preproces import Preprocessor
from src.feature_extraction import FeatureExtractor
from src.label_encoder import LabelEncoderClass
from src.train_model import TrainModel


class Predictor:

    def __init__(self):

        self.feature = FeatureExtractor()

        self.feature.loadVectorizer()

        self.encoder = LabelEncoderClass()

        self.encoder.loadEncoder()

        self.model = TrainModel()

        self.model.loadModel()

    # Predict User Intent
    def predict(self, user_text):

        # Preprocess user input
        process = Preprocessor(user_text)

        clean_text = " ".join(process.preprocess())

        # Convert into TF-IDF vector
        vector = self.feature.transform([clean_text])

        # Predict label
        prediction = self.model.best_model.predict(vector)

        # Convert number back into tag
        tag = self.encoder.inverse_transform(prediction)

        return tag[0]