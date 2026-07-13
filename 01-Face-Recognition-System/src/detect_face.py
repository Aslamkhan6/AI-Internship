import cv2

from src.camera import CameraManager


def detect_faces():

    camera = CameraManager()

    print("Face Detection Started")

    while True:

        frame = camera.read()

        if frame is None:
            break

        faces = camera.detect(
            frame
        )

        camera.draw(
            frame,
            faces
        )

        cv2.putText(
            frame,
            f"Faces : {len(faces)}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        camera.show(
            "Face Detection",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()