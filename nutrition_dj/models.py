from django.db import models

# Create your models here.
class FoodProduct(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    megethos = models.CharField(max_length=2)
    energyCal = models.FloatField(default=0)
    energykJ = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    carb = models.FloatField(default=0)
    total_fat = models.FloatField(default=0)