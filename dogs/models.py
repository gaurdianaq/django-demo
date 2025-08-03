from django.db import models

# Create your models here.


class Breed(models.Model):
    SIZES = {"XS": "Extra Small", "S": "Small", "M": "Medium", "L": "Large", "XL": "Extra Large"}
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=2, choices=SIZES, default="M")


class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
