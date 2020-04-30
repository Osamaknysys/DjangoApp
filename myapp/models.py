from django.db import models

# Create your models here.
class Ingredient(models.Model):
    Ingredient_title = models.CharField(max_length=200)
    Ingredient_quantity = models.CharField(max_length=200)
    Ingredient_price = models.IntegerField()
    Ingredient_expir = models.BooleanField()