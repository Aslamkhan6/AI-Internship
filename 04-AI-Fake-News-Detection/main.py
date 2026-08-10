from src.dataset import DatasetLoader
from src.preprocessor import Preprocessor
from src.feature_extraction import FeatureExtractor
from src.label_encoder import LabelEncoderClass
from src.train_model import TrainModel

from sklearn.model_selection import train_test_split


def main():

    print("=" * 60)
    print(" AI Fake News Detection System - Model Training")
    print("=" * 60)

    # ==========================================
    # Load Dataset
    # ==========================================

    dataset = DatasetLoader()

    dataset.loadData()

    dataset.checkData()

    X, Y = dataset.prepareData()

    # ==========================================
    # Preprocess Dataset
    # ==========================================

    print("\nPreprocessing News Articles...")

    clean_text = []

    total = len(X)

    for index, article in enumerate(X, start=1):

        processor = Preprocessor(article)

        clean_article = " ".join(
            processor.preprocess()
        )

        clean_text.append(clean_article)

        # Progress after every 5000 articles
        if index % 5000 == 0 or index == total:

            print(f"Processed {index}/{total}")

    print("Preprocessing Completed Successfully.")

    # ==========================================
    # Feature Extraction
    # ==========================================

    print("\nExtracting TF-IDF Features...")

    feature = FeatureExtractor(clean_text)

    X = feature.fit_transform()

    print("Feature Extraction Completed.")

    # ==========================================
    # Label Encoding
    # ==========================================

    encoder = LabelEncoderClass()

    Y = encoder.fit_transform(Y)

    print("Labels Encoded Successfully.")

    # ==========================================
    # Split Dataset
    # ==========================================

    X_train, X_test, Y_train, Y_test = train_test_split(

        X,

        Y,

        test_size=0.20,

        random_state=42,

        stratify=Y

    )

    print("\nDataset Split Successfully.")

    print(f"Training Samples : {X_train.shape[0]}")

    print(f"Testing Samples  : {X_test.shape[0]}")

    # ==========================================
    # Train Models
    # ==========================================

    trainer = TrainModel()

    trainer.train(

        X_train,

        Y_train,

        X_test,

        Y_test

    )

    # ==========================================
    # Save Files
    # ==========================================

    trainer.saveModel()

    feature.saveVectorizer()

    encoder.saveEncoder()

    # ==========================================
    # Training Completed
    # ==========================================

    print("\n" + "=" * 60)

    print(" Training Completed Successfully.")

    print("=" * 60)


if __name__ == "__main__":

    main()