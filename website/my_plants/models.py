from django.db import models


class Plants(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    scientific_name = models.CharField(unique=True, max_length=200, default='none')

    light = models.TextField(default='medium')
    water = models.TextField(default='medium')
    soil = models.TextField(default='wet')
    temperature = models.TextField(default='medium')

    persian_name = models.CharField(max_length=100, default='گیاه')



    def __str__(self):
        return self.name
