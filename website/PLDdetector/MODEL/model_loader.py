from tensorflow.keras.models import load_model

model_path = './plant_leaf_deseases_detector.h5'
model = load_model(model_path)

def model_loader():

    return 'succesful'
