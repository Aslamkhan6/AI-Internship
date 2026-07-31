import json
import os
from src.config import DATASET_FILE


class DataLoader:
    def getPatterns(self):
        return self.patterns


    def getTags(self):
        return self.tags


    def getResponses(self):
        return self.responses
    def __init__(self):
        self.dataset_path = DATASET_FILE
        self.patterns = []
        self.tags = []
        self.responses = {}


    def loadData(self):

        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(
            f"Dataset not found: {self.dataset_path}"
        )

        with open(self.dataset_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data


    def prepareData(self):

         data = self.loadData()

         for intent in data["intents"]:

             tag = intent["tag"]

             self.responses[tag] = intent["responses"]

             for pattern in intent["patterns"]:

                 self.patterns.append(pattern)
                 self.tags.append(tag)

         return self.patterns, self.tags     