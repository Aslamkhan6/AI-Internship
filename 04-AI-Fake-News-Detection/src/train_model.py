import joblib

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

from src.config import MODEL_FILE


class TrainModel:

    def __init__(self):

        self.models = {

            "MultinomialNB": MultinomialNB(),

            "LogisticRegression": LogisticRegression(
                max_iter=1000,
                random_state=42
            ),

            "LinearSVC": LinearSVC(
                random_state=42
            )

        }

        self.best_model = None
        self.best_accuracy = 0
        self.best_model_name = ""

    # ==========================================
    # Train All Models
    # ==========================================

    def train(self, X_train, Y_train, X_test, Y_test):

        print("\n" + "=" * 50)
        print("Training Models")
        print("=" * 50)

        for name, model in self.models.items():

            # Train model
            model.fit(X_train, Y_train)

            # Predict
            prediction = model.predict(X_test)

            # Accuracy
            accuracy = accuracy_score(
                Y_test,
                prediction
            )

            print(f"{name:<25}: {accuracy * 100:.2f}%")

            # Best Model
            if accuracy > self.best_accuracy:

                self.best_accuracy = accuracy
                self.best_model = model
                self.best_model_name = name

        print("\n" + "=" * 50)
        print(f"Best Model : {self.best_model_name}")
        print(f"Accuracy   : {self.best_accuracy * 100:.2f}%")
        print("=" * 50)

    # ==========================================
    # Save Best Model
    # ==========================================

    def saveModel(self):

        if self.best_model is None:

            raise Exception("No trained model available.")

        joblib.dump(

            self.best_model,

            MODEL_FILE

        )

        print("\nModel Saved Successfully.")

    # ==========================================
    # Load Saved Model
    # ==========================================

    @staticmethod
    def loadModel():

        return joblib.load(MODEL_FILE)