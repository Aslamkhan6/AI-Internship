import os
import tkinter as tk
from tkinter import messagebox

import joblib
from sklearn.model_selection import train_test_split

from src.config import MODEL_DIR
from src.datasets import Emotiondataset
from src.Emotion_prediction import EmotionPredictor
from src.feature_extraction import FeatureExtractor
from src.preproces import Preprocessor
from src.train_model import Trainmodel


MODEL_PATH = os.path.join(MODEL_DIR, "emotion_model.joblib")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "emotion_vectorizer.joblib")


class EmotionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Detector")
        self.root.geometry("650x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#f3f6fb")

        self.status_var = tk.StringVar(value="Preparing model...")
        self.result_var = tk.StringVar(value="Your prediction will appear here.")

        self.build_ui()
        self.ensure_model_ready()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="Text Emotion Detector",
            font=("Segoe UI", 20, "bold"),
            bg="#f3f6fb",
            fg="#1f2937",
        )
        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            self.root,
            text="Type a sentence and predict its emotion",
            font=("Segoe UI", 11),
            bg="#f3f6fb",
            fg="#4b5563",
        )
        subtitle.pack(pady=(0, 15))

        frame = tk.Frame(self.root, bg="#ffffff", bd=1, relief="groove")
        frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.text_box = tk.Text(frame, height=9, width=70, font=("Segoe UI", 12), wrap="word")
        self.text_box.pack(padx=15, pady=15)

        button_frame = tk.Frame(frame, bg="#ffffff")
        button_frame.pack(pady=(0, 10))

        predict_btn = tk.Button(
            button_frame,
            text="Predict Emotion",
            width=18,
            bg="#2563eb",
            fg="white",
            bd=0,
            command=self.predict_emotion,
        )
        predict_btn.pack(side="left", padx=8)

        train_btn = tk.Button(
            button_frame,
            text="Train Model",
            width=15,
            bg="#10b981",
            fg="white",
            bd=0,
            command=self.train_model,
        )
        train_btn.pack(side="left", padx=8)

        status_label = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Segoe UI", 10),
            bg="#f3f6fb",
            fg="#374151",
        )
        status_label.pack(pady=(8, 4))

        result_label = tk.Label(
            self.root,
            textvariable=self.result_var,
            font=("Segoe UI", 12, "bold"),
            bg="#f3f6fb",
            fg="#111827",
            wraplength=550,
        )
        result_label.pack(pady=(4, 10))

    def ensure_model_ready(self):
        if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
            self.status_var.set("Model ready. You can start predicting.")
            return

        self.train_model(show_message=False)

    def train_model(self, show_message=True):
        try:
            self.status_var.set("Training model, please wait...")
            self.root.update_idletasks()

            emotion_data = Emotiondataset()
            data = emotion_data.loaddata()
            text = data["text"].astype(str).tolist()
            label = data["emotion"]

            clean_text = []
            for sentence in text:
                process = Preprocessor(sentence)
                clean_text.append(" ".join(process.preprocess()))

            feature = FeatureExtractor(clean_text)
            converted_data = feature.fit_transform()

            X_train, X_test, Y_train, Y_test = train_test_split(
                converted_data,
                label,
                test_size=0.2,
                random_state=42,
            )

            trainer = Trainmodel()
            trainer.train(X_train, Y_train)
            accuracy = trainer.test(X_test, Y_test)
            trainer.save_model(MODEL_PATH)
            joblib.dump(feature.vectorizer, VECTORIZER_PATH)

            self.status_var.set(f"Model trained successfully. Accuracy: {accuracy:.2%}")
            if show_message:
                messagebox.showinfo("Success", f"Model trained successfully.\nAccuracy: {accuracy:.2%}")
        except Exception as exc:
            self.status_var.set("Training failed")
            if show_message:
                messagebox.showerror("Error", f"Training failed:\n{exc}")
            raise

    def predict_emotion(self):
        user_text = self.text_box.get("1.0", "end").strip()
        if not user_text:
            messagebox.showwarning("Empty input", "Please enter some text first.")
            return

        if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
            self.train_model(show_message=False)

        self.status_var.set("Predicting emotion...")
        self.root.update_idletasks()

        predictor = EmotionPredictor(MODEL_PATH, VECTORIZER_PATH)
        emotion = predictor.predict_emottion(user_text)
        self.result_var.set(f"Predicted emotion: {emotion}")
        self.status_var.set("Prediction complete")


def main():
    root = tk.Tk()
    EmotionGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()