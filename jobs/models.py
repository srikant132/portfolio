from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')  #here image model and source to save value
    summary = models.CharField(max_length=200)
