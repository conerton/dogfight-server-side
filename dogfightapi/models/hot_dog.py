from django.db import models
# from django.contrib.auth.models import User


class HotDog(models.Model):

    name = models.CharField(max_length=50)
    toppings = models.CharField(max_length=500)
    image = models.CharField(max_length=10)
