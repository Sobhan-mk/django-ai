from django.db import models


class Plants(models.Model):
    name = models.CharField(unique=True, max_length=100)
    scientific_name = models.CharField(unique=True, max_length=200, default='')
    persian_name = models.CharField(max_length=100, default='')

    description = models.TextField(default='')

    conditions = models.TextField(default='')

    deseases = models.TextField(default='')

    plant_image = models.ImageField(upload_to='plant_images/', null=True, blank=True)

    def __str__(self):
        return self.name
