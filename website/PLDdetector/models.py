from django.db import models


class PlantLeaf(models.Model):
    image = models.ImageField(upload_to='plant_leaf_images')