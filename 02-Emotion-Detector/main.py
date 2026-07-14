from src.datasets import Emotiondataset

def main():
    emotion_data =  Emotiondataset()
    emotion_data.loaddata()
    emotion_data.checkdata()
    





if __name__ =="__main__":
    main()
