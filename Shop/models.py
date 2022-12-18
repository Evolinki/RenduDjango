from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)
    
class Product(models.Model):
    
    Url_Image = models.CharField(max_length=200)
    Nom = models.TextField()
    stock = models.IntegerField()
    prix = models.IntegerField()