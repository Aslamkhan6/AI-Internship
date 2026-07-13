import os
import json
import cv2

from src.camera import CameraManager

from src.config import (
    MODEL_FILE,
    LABELS_FILE
)


class FaceRecognizer:

    def __init__(self):

        self.camera = CameraManager()

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

        self.labels = {}

        self.load_model()

        self.load_labels()


    def load_model(self):
        """
        Load trained LBPH model.
        """

        if not os.path.exists(MODEL_FILE):
            raise FileNotFoundError(
                "trainer.yml not found.\nPlease train the model first."
            )

        self.recognizer.read(MODEL_FILE)


    def load_labels(self):
        """
        Load labels.json.
        """

        if not os.path.exists(LABELS_FILE):
            raise FileNotFoundError(
                "labels.json not found."
            )

        with open(
            LABELS_FILE,
            "r"
        ) as file:

            self.labels = json.load(file)


    def predict_face(self, frame, face):

        x, y, w, h = face

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        face_image = gray[
            y:y+h,
            x:x+w
        ]

        face_image = cv2.resize(
            face_image,
            (200, 200)
        )

        label, confidence = self.recognizer.predict(
            face_image
        )

        return label, confidence


    def start(self):
        """
        Start real-time face recognition.
        """

        print("\n====================================")
        print(" FACE RECOGNITION STARTED")
        print(" Press 'Q' to Quit")
        print("====================================")

        while True:

            frame = self.camera.read()

            if frame is None:
                break

            faces = self.camera.detect(frame)

            self.camera.draw(frame, faces)

            for face in faces:

                x, y, w, h = face

                try:

                    label, confidence = self.predict_face(
                        frame,
                        face
                    )

                    # Lower confidence = Better Match
                    if confidence < 70:

                        person_name = self.labels.get(
                            str(label),
                            "Unknown"
                        )

                        color = (0, 255, 0)

                        text = f"{person_name} ({confidence:.1f})"

                    else:

                        color = (0, 0, 255)

                        text = f"Unknown ({confidence:.1f})"

                    cv2.putText(
                        frame,
                        text,
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        color,
                        2
                    )

                except Exception as error:

                    print(error)

            self.camera.show(
                "AI Face Recognition",
                frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        self.camera.release()

        print("\nFace Recognition Stopped.")


if __name__ == "__main__":

    recognizer = FaceRecognizer()

    recognizer.start()   