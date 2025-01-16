from django.db import models
from accounts.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=100)
    detail = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


