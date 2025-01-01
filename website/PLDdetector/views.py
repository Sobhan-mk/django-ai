from django.shortcuts import render
from .forms import PlantLeafForm
from PIL import Image
from django.contrib import messages
from tensorflow.keras.models import load_model
import numpy as np
import os

def detector_model(request):
    prediction = None
    if request.method == 'POST':
        form = PlantLeafForm(request.POST, request.FILES)

        if form.is_valid():
            image_saved = form.save()
            image = image_saved.image

            with Image.open(image.path) as img:
                if img.size[0] == img.size[1]:
                    img = img.resize((256, 256))
                    arr_img = np.array(img)
                    expanded_img_array = np.expand_dims(arr_img, axis=0)

                    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                    model_path = os.path.join(BASE_DIR, 'plant_leaf_deseases_detector.h5')
                    model = load_model(model_path)

                    prediction = model.predict(expanded_img_array)
                    predicted_class = np.argmax(prediction, axis=-1)
                    messages.success(request, str(len(prediction[0])), 'success')


                else:
                    messages.success(request, 'the shape of image should be square')

    form = PlantLeafForm()

    return render(request, 'PLDdetector/detector_model.html', {'form': form, 'prediction': prediction})

