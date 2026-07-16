from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import joblib


class Trainmodel:
    def __init__(self):
        self.model = LinearSVC()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def test(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)
        print("model saved successfully at", model_path)
