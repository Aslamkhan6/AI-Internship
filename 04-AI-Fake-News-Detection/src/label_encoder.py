import joblib

from sklearn.preprocessing import LabelEncoder

from src.config import ENCODER_FILE


class LabelEncoderClass:

    def __init__(self):

        self.encoder = LabelEncoder()

    # ==========================================
    # Fit and Transform Labels
    # ==========================================

    def fit_transform(self, labels):

        return self.encoder.fit_transform(labels)

    # ==========================================
    # Transform New Labels
    # ==========================================

    def transform(self, labels):

        return self.encoder.transform(labels)

    # ==========================================
    # Decode Prediction
    # ==========================================

    def inverse_transform(self, labels):

        return self.encoder.inverse_transform(labels)

    # ==========================================
    # Save Encoder
    # ==========================================

    def saveEncoder(self):

        joblib.dump(

            self.encoder,

            ENCODER_FILE

        )

        print("Label Encoder Saved Successfully.")

    # ==========================================
    # Load Encoder
    # ==========================================

    @staticmethod
    def loadEncoder():

        return joblib.load(ENCODER_FILE)