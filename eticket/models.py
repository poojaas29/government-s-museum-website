from django.db import models
from django.contrib.auth.models import User


class Visitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=30)
    phone = models.IntegerField()
    nationality = models.CharField(max_length=30)
    address = models.CharField(max_length=150)


def __str__(self):
    return self.user.user


class Booking_Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    museumname = models.CharField(max_length=40)
    dov = models.DateField(max_length=20)
    time = models.TimeField(max_length=30)
    nob = models.IntegerField()


def __str__(self):
    return self.user.user


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    booking_detail = models.ForeignKey(
        Booking_Detail, on_delete=models.CASCADE)
    qrcode = models.ImageField()


# class Show(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     museum_name = models.CharField(max_length=40)
#     time_slot = models.TimeField(max_length=30)
#     date = models.DateField(max_length=20)
#     price = models.IntegerField()

# def __str__(self):
#         return self.user.username
