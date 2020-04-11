from django.db import models

# Create your models here.

class Events(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    button_text=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')
