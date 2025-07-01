from django.db import models
from django.urls import reverse

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    street = models.ForeignKey('Street', on_delete=models.CASCADE)
    house = models.SlugField(max_length=255)
    time_open = models.TimeField()
    time_close = models.TimeField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
