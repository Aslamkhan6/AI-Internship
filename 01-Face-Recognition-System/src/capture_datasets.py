import os
import time
import cv2

from src.config import (
    DATASET_DIR,
    IMAGES_PER_PERSON
)

from src.camera import CameraManager

from src.utils import (
    create_person_folder,
    crop_face,
    preprocess_face,
    save_face,
    draw_status
)


class DatasetCollector:

    def __init__(self):

        # Camera Manager
        self.camera = CameraManager()

        # Person Information
        self.person_name = ""
        self.person_folder = ""
# Dataset Information
        self.image_count = 0          # Total images in folder
        self.new_images = 0           # Images captured in current session
        self.target_images = IMAGES_PER_PERSON

        # Capture Settings
        self.capture_started = False
        self.capture_delay = 1.5
        self.last_capture_time = 0


    def get_person_name(self):

        while True:

            name = input("\nEnter Person Name : ").strip()

            if len(name) >= 2:
                return name

            print("Invalid Name.")


    def prepare_dataset(self):

        self.person_name = self.get_person_name()

        self.person_folder = create_person_folder(
            DATASET_DIR,
            self.person_name
        )

        images = [
            file
            for file in os.listdir(self.person_folder)
            if file.endswith(".jpg")
        ]

        self.image_count = len(images)
        self.new_images = 0


    def should_capture(self):

        current_time = time.time()

        if current_time - self.last_capture_time >= self.capture_delay:

            self.last_capture_time = current_time

            return True

        return False


    def save_face_image(self, frame, face):

        face_image = crop_face(
            frame,
            face
        )

        face_image = preprocess_face(
            face_image
        )

        self.image_count += 1
        self.new_images += 1

        save_face(
    face_image,
    self.person_folder,
    self.image_count
)


    def start(self):

        self.prepare_dataset()

        print("\n==============================")
        print("DATASET COLLECTION STARTED")
        print("==============================")
        print("Press C -> Start Capture")
        print("Press Q -> Quit")
        print("==============================")

        while True:

            frame = self.camera.read()

            if frame is None:
                break

            faces = self.camera.detect(
                frame
            )

            self.camera.draw(
                frame,
                faces
            )

            draw_status(
    frame,
    self.person_name,
    self.new_images,
    self.target_images,
    self.capture_started
)
            print('CAPTURING  THE IMAGE ')           # Start capturing when user presses C
            if self.capture_started:

                # Only save if exactly one face is detected
                if len(faces) == 1:

                    if self.should_capture():

                        self.save_face_image(
                            frame,
                            faces[0]
                        )

                elif len(faces) > 1:

                    cv2.putText(
                        frame,
                        "Multiple Faces Detected!",
                        (20, 170),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 0, 255),
                        2
                    )

                else:

                    cv2.putText(
                        frame,
                        "No Face Detected!",
                        (20, 170),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 0, 255),
                        2
                    )

            # Dataset completed
            if self.new_images >= self.target_images:

                cv2.putText(
                    frame,
                    "Dataset Collection Completed!",
                    (20, 210),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

                self.camera.show(
                    "Dataset Collection",
                    frame
                )

                cv2.waitKey(2000)

                break

            # Show live webcam
            self.camera.show(
                "Dataset Collection",
                frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("c"):

                self.capture_started = True

            elif key == ord("q"):

                break

        # Release Camera
        self.camera.release()

        print("\n=================================")
        print(" Dataset Collection Completed")
        print("=================================")
        print(f"Person Name : {self.person_name}")
        print(f"Images Saved: {self.image_count}")
        print("=================================")


if __name__ == "__main__":

    collector = DatasetCollector()

    collector.start()