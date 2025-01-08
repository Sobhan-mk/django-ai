from django.shortcuts import render
from .forms import PlantLeafForm
from PIL import Image
from django.contrib import messages
#from .MODEL.model_loader import model_loader

def detector_model(request):
    prediction = None
    if request.method == 'POST':
        form = PlantLeafForm(request.POST, request.FILES)

        if form.is_valid():
            image_saved = form.save()
            image = image_saved.image

            with Image.open(image.path) as img:
                if img.size[0] == img.size[1]:

                    #prediction_class = model_loader(img)

                    messages.success(request, 'alright', 'success')


                else:
                    messages.success(request, 'the shape of image should be square')

    form = PlantLeafForm()

    return render(request, 'PLDdetector/detector_model.html', {'form': form, 'prediction': prediction})

