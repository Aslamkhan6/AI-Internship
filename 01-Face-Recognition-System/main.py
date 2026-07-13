from src.detect_face import detect_faces
from src.capture_datasets import DatasetCollector
from src.train_model import  FaceTrainer
from src.rocognize_face import FaceRecognizer

def main():

    while True:

        print("\n========== AI FACE DETECTION & RECOGNITION ==========")
        print("1. Detect Face")
        print("2. Register New Face")
        print("3. Train Model")
        print("4. Recognize Face")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            detect_faces()
      

        if choice == "2":

            datacolletor =   DatasetCollector()
            datacolletor.start()

        if choice == "3":
            facetrainer = FaceTrainer()
            facetrainer.start()    

        if choice == "4":
            recognizer = FaceRecognizer()

            recognizer.start()    

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("wrong  input.")


if __name__ == "__main__":
    main()