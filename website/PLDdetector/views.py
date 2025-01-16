from django.shortcuts import render
from .forms import PlantLeafForm
from PIL import Image
from django.contrib import messages
#from .MODEL.model_loader import model_loader
import random
import os

def detector_model(request):
    prediction = None
    image_url = ''
    image_shape = None
    if request.method == 'POST':
        form = PlantLeafForm(request.POST, request.FILES)

        if form.is_valid():
            image_saved = form.save()
            image = image_saved.image
            image_url = image.url

            with Image.open(image.path) as img:
                if img.size[0] == img.size[1]:

                    #prediction_class = model_loader(img)
                    image_shape = True

                else:
                    image_shape = False

    form = PlantLeafForm()

    random_indexes = [random.randint(0, 37) for _ in range(10)]

    example_files_path = 'C:/Users/sobha/Desktop/django-ai/website/static/pld_example_images'

    example_images = [os.path.join('pld_example_images', os.listdir(example_files_path)[i]) for i in random_indexes]

    return render(request, 'PLDdetector/detector_model.html', {'form': form, 'prediction': prediction, 'image_url': image_url, 'image_shape' : image_shape, 'random_samples' : example_images})

