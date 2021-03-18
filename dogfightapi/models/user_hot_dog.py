from django.db import models
from django.contrib.auth.models import User
from .hot_dog import HotDog


class UserHotDog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hot_dog = models.ForeignKey("HotDog", on_delete=models.CASCADE, null=True)
    date_completed = models.IntegerField(null=True)
    is_favorite = models.BooleanField(null=True)
    note = models.CharField(max_length=100, null=True)
    is_approved = models.BooleanField(null=True)
