from django.db import models


# Create your models here.

class Rented_Bikes(models.Model):
    username = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=20, null=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    bike = models.CharField(max_length=20, null=True)
    amount = models.IntegerField(null=True)
    otp = models.IntegerField(null=True)

    def __str__(self):
        return self.username + " - " + self.bike


class Available_Bikes(models.Model):
    name = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=20, null=True)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.name + " - " + self.location
