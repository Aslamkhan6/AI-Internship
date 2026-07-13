import os
import cv2

from src.config import (
    HAAR_CASCADE_PATH,
    IMAGE_SIZE
)


def load_face_detector():
    """
    Load the Haar Cascade face detector.
    """

    detector = cv2.CascadeClassifier(HAAR_CASCADE_PATH)

    if detector.empty():
        raise FileNotFoundError(
            f"Unable to load Haar Cascade model.\n"
            f"Expected Location:\n{HAAR_CASCADE_PATH}"
        )

    return detector


def open_camera(camera_index=0):
    """
    Open webcam.
    """

    camera = cv2.VideoCapture(camera_index)

    if not camera.isOpened():
        raise RuntimeError("Unable to access webcam.")

    return camera


def create_person_folder(dataset_path, person_name):
    """
    Create a folder for a new person.
    """

    person_name = person_name.strip()

    folder_path = os.path.join(
        dataset_path,
        person_name
    )

    os.makedirs(folder_path, exist_ok=True)

    return folder_path


def crop_face(image, face):
    """
    Crop detected face.
    """

    x, y, w, h = face

    return image[y:y+h, x:x+w]


def preprocess_face(face_image):
    """
    Convert face into standard format.
    """

    gray = cv2.cvtColor(
        face_image,
        cv2.COLOR_BGR2GRAY
    )

    resized = cv2.resize(
        gray,
        IMAGE_SIZE
    )

    return resized


def save_face(face_image, folder_path, image_number):
    """
    Save face image.
    """

    filename = os.path.join(
        folder_path,
        f"{image_number}.jpg"
    )

    cv2.imwrite(
        filename,
        face_image
    )


def draw_face_boxes(frame, faces):
    """
    Draw rectangle around faces.
    """

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )


def draw_status(
    frame,
    person_name,
    captured,
    total,
    started
):
    """
    Draw information panel.
    """

    status = (
        "Capturing"
        if started
        else
        "Waiting"
    )

    cv2.putText(
        frame,
        "AI FACE DETECTION & RECOGNITION",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Person : {person_name}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Captured : {captured}/{total}",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Status : {status}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Press C : Start Capture",
        (20, 430),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Press Q : Quit",
        (20, 460),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )


def close_camera(camera):
    """
    Release webcam resources.
    """

    camera.release()

    cv2.destroyAllWindows()


def detect_faces(detector, frame):

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = detector.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(60,60)
    )

    return faces  