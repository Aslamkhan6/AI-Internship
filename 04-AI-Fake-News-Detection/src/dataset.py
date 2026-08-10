import pandas as pd

from src.config import (
    FAKE_DATASET,
    TRUE_DATASET
)


class DatasetLoader:

    def __init__(self):

        self.data = None

    # ==========================
    # Load Dataset
    # ==========================

    def loadData(self):

        fake = pd.read_csv(FAKE_DATASET)

        true = pd.read_csv(TRUE_DATASET)

        # Add Labels
        fake["label"] = "Fake"

        true["label"] = "Real"

        # Merge datasets
        self.data = pd.concat(
            [fake, true],
            ignore_index=True
        )

        # Shuffle dataset
        self.data = self.data.sample(
            frac=1,
            random_state=42
        ).reset_index(drop=True)

        print("Dataset Loaded Successfully")

        return self.data

    # ==========================
    # Prepare Dataset
    # ==========================

    def prepareData(self):

        if self.data is None:

            self.loadData()

        # Combine title and article
        self.data["content"] = (
            self.data["title"].fillna("")
            + " "
            + self.data["text"].fillna("")
        )

        X = self.data["content"]

        Y = self.data["label"]

        return X, Y

    # ==========================
    # Check Dataset
    # ==========================

    def checkData(self):

        if self.data is None:

            self.loadData()

        print("\n========== First 5 Rows ==========\n")

        print(self.data.head())

        print("\n========== Dataset Shape ==========\n")

        print(self.data.shape)

        print("\n========== Missing Values ==========\n")

        print(self.data.isnull().sum())

        print("\n========== Label Distribution ==========\n")

        print(self.data["label"].value_counts())