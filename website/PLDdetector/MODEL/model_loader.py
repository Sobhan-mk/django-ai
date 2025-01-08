from tensorflow.keras.models import load_model
import os
import numpy as np


def model_loader(img):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(BASE_DIR, 'MODEL', 'plant_leaf_deseases_detector.h5')
    model = load_model(model_path)

    img = img.resize((256, 256))
    arr_img = np.array(img)
    expanded_img_array = np.expand_dims(arr_img, axis=0)
    image = expanded_img_array / 255.0

    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=-1)

    return predicted_class