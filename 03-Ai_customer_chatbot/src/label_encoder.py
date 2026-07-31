from sklearn.preprocessing import LabelEncoder
import joblib

from src.config import LABEL_ENCODER_FILE


class LabelEncoderClass:

    def __init__(self):

        self.encoder = LabelEncoder()

    # Convert labels into numbers
    def fit_transform(self, labels):

        return self.encoder.fit_transform(labels)

    # Convert predicted number back into text
    def inverse_transform(self, label):

        return self.encoder.inverse_transform(label)

    # Save encoder
    def saveEncoder(self):

        joblib.dump(self.encoder, LABEL_ENCODER_FILE)

        print("Label Encoder Saved Successfully.")

    # Load encoder
    def loadEncoder(self):

        self.encoder = joblib.load(LABEL_ENCODER_FILE)

        return self.encoder