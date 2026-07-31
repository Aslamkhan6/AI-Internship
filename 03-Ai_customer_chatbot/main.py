from src.data_loader import DataLoader
from src.preproces import Preprocessor
from src.feature_extraction import FeatureExtractor
from src.label_encoder import LabelEncoderClass
from src.train_model import TrainModel

from sklearn.model_selection import train_test_split


def main():

    # ==========================
    # Load Dataset
    # ==========================

    data = DataLoader()

    patterns, tags = data.prepareData()

    # ==========================
    # Preprocess Patterns
    # ==========================

    clean_patterns = []

    for sentence in patterns:

        process = Preprocessor(sentence)

        clean_patterns.append(
            " ".join(process.preprocess())
        )

    # ==========================
    # Feature Extraction
    # ==========================

    feature = FeatureExtractor(clean_patterns)

    X = feature.fit_transform()

    # ==========================
    # Encode Labels
    # ==========================

    encoder = LabelEncoderClass()

    Y = encoder.fit_transform(tags)

    # ==========================
    # Split Dataset
    # ==========================

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    # ==========================
    # Train Models
    # ==========================

    trainer = TrainModel()

    trainer.train(
        X_train,
        Y_train,
        X_test,
        Y_test
    )

    # ==========================
    # Save Everything
    # ==========================

    trainer.saveModel()

    feature.saveVectorizer()

    encoder.saveEncoder()

    print("\nTraining Completed Successfully.")


if __name__ == "__main__":

    main()