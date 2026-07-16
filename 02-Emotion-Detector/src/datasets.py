import os
import pandas as pd

from src.config import DATASET_FILE


class Emotiondataset:

    def __init__(self):
        self.datasetpath = DATASET_FILE
        self.dataframe = None

    # load dataset
    def loaddata(self):

        if not os.path.exists(self.datasetpath):
            raise FileNotFoundError(
                f"\nDataset not found:\n{self.datasetpath}"
            )

        self.dataframe = pd.read_csv(
       self.datasetpath,
       sep=";",
       names=["text", "emotion"],
       header = None
)

        print("Dataset loaded successfully")

        return self.dataframe

    # check the dataset
    def checkdata(self):

        if self.dataframe is None:
            raise ValueError("Data not found in dataset")

        print("#### datasets data ####")

        print(
            self.dataframe.head(10)
        )

        print("#### datasets null value ####")

        print(
            self.dataframe.isnull().sum()
        )
        print(self.dataframe.describe())
        print("#### datasets data ####")

    # get the dataset
    def getdataframe(self):
       
       return self.dataframe