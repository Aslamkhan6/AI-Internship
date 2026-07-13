import os
import json
import cv2
import numpy as np

from src.config import (
    DATASET_DIR,
    MODEL_FILE,
    LABELS_FILE
)


class FaceTrainer:
    """
    Train the LBPH Face Recognition model.
    """

    def __init__(self):

        self.dataset_path = DATASET_DIR
        self.model_path = MODEL_FILE
        self.labels_path = LABELS_FILE

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

        self.faces = []
        self.labels = []

        self.label_map = {}

        self.current_label = 0


    def load_dataset(self):
        """
        Load every image from the dataset folder.
        """

        print("\nLoading Dataset...\n")

        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(
                f"Dataset folder not found:\n{self.dataset_path}"
            )

        persons = sorted(os.listdir(self.dataset_path))

        for person in persons:

            person_folder = os.path.join(
                self.dataset_path,
                person
            )

            if not os.path.isdir(person_folder):
                continue

            print(f"Reading images of {person}")

            self.label_map[self.current_label] = person

            for image_name in os.listdir(person_folder):

                if not image_name.lower().endswith(
                    (".jpg", ".jpeg", ".png")
                ):
                    continue

                image_path = os.path.join(
                    person_folder,
                    image_name
                )

                image = cv2.imread(
                    image_path,
                    cv2.IMREAD_GRAYSCALE
                )

                if image is None:
                    print(f"Skipped: {image_name}")
                    continue

                self.faces.append(image)

                self.labels.append(
                    self.current_label
                )

            self.current_label += 1

        if len(self.faces) == 0:

            raise RuntimeError(
                "No training images found."
            )

        print(
            f"\nLoaded {len(self.faces)} images."
        )


    def train_model(self):
        """
        Train the LBPH recognizer.
        """

        print("\nTraining Model...")

        self.recognizer.train(
            self.faces,
            np.array(self.labels)
        )

        print("Model trained successfully.")


    def save_model(self):
        """
        Save the trained model.
        """

        self.recognizer.write(
            self.model_path
        )

        print(f"\nModel Saved:")
        print(self.model_path)


    def save_labels(self):
        """
        Save label mapping.
        """

        with open(
            self.labels_path,
            "w"
        ) as file:

            json.dump(
                self.label_map,
                file,
                indent=4
            )

        print(f"Labels Saved:")
        print(self.labels_path)


    def print_summary(self):
        """
        Display training summary.
        """

        print("\n====================================")
        print("       TRAINING COMPLETED")
        print("====================================")
        print(f"Total Persons : {len(self.label_map)}")
        print(f"Total Images  : {len(self.faces)}")
        print("====================================")


    def start(self):
        """
        Complete training pipeline.
        """

        try:

            self.load_dataset()

            self.train_model()

            self.save_model()

            self.save_labels()

            self.print_summary()

        except Exception as error:

            print("\nTraining Failed!")
            print(error)


if __name__ == "__main__":

    trainer = FaceTrainer()

    trainer.start()    