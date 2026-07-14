import os 

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


DATA_DIR = os.path.join(BASE_DIR, 'data')
MODEL_DIR = os.path.join(BASE_DIR,'model')

DATASET_FILE = os.path.join(DATA_DIR,'train.csv')


requires_directories = [
    
    DATA_DIR,
    MODEL_DIR
]


for directory in requires_directories:
    os.makedirs(directory,exist_ok=True)