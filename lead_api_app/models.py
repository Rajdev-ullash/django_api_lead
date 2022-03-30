from django.db import models

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="picture", blank=True)
    def __str__(self):
        return self.name
    
