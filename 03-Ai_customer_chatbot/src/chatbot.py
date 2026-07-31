import random

from src.data_loader import DataLoader
from src.predictor import Predictor


class ChatBot:

    def __init__(self):

        # Load all responses
        self.data = DataLoader()

        self.data.prepareData()

        self.responses = self.data.getResponses()

        # Load predictor
        self.predictor = Predictor()

    # Chat with user
    def chat(self, user_text):

        # Predict intent
        tag = self.predictor.predict(user_text)

        # Get responses of that intent
        response_list = self.responses[tag]

        # Select one response randomly
        response = random.choice(response_list)

        return response