from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

import joblib

from src.config import MODEL_FILE


class TrainModel:

    def __init__(self):

        self.models = {

            "MultinomialNB": MultinomialNB(),

            "LogisticRegression": LogisticRegression(max_iter=1000),

            "LinearSVC": LinearSVC()

        }

        self.best_model = None
        self.best_accuracy = 0

    # Train all models
    def train(self, X_train, Y_train, X_test, Y_test):

        for name, model in self.models.items():

            model.fit(X_train, Y_train)

            prediction = model.predict(X_test)

            accuracy = accuracy_score(Y_test, prediction)

            print(f"{name} : {accuracy * 100:.2f}%")

            if accuracy > self.best_accuracy:

                self.best_accuracy = accuracy
                self.best_model = model

        print("\nBest Model :", type(self.best_model).__name__)
        print(f"Accuracy : {self.best_accuracy * 100:.2f}%")

    # Save Best Model
    def saveModel(self):

        joblib.dump(self.best_model, MODEL_FILE)

        print("Model saved successfully.")

    # Load Saved Model
    def loadModel(self):

        self.best_model = joblib.load(MODEL_FILE)

        return self.best_model