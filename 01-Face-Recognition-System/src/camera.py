import cv2

from src.utils import (
    load_face_detector,
    detect_faces,
    draw_face_boxes,
    close_camera
)


class CameraManager:

    def __init__(self):

        self.detector = load_face_detector()

        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise RuntimeError("Unable to open webcam.")


    def read(self):

        success, frame = self.camera.read()

        if not success:
            return None

        return frame


    def detect(self, frame):

        return detect_faces(
            self.detector,
            frame
        )


    def draw(self, frame, faces):

        draw_face_boxes(
            frame,
            faces
        )


    def show(self, title, frame):

        cv2.imshow(
            title,
            frame
        )


    def release(self):

        close_camera(
            self.camera
        )