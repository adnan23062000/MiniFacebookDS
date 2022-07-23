from django.db import models
from django.utils import timezone

# Create your models here.

class Material(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(default=timezone.now)
    pdf = models.FileField(upload_to='materials/')

    def __str__(self):
        return self.title
