from django.db import models

# Extend the user model
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    vacancy = models.CharField(max_length=30, blank=True)
    competences = models.CharField(max_length=30, blank=True)
    driverslicence = models.CharField(max_length=30, blank=True)
    primary_phone = models.CharField(max_length=30, blank=True)
    secondary_phone = models.CharField(max_length=30, blank=True)
    telegram_id = models.CharField(max_length=60, blank=True)
    street_address = models.CharField(max_length=60, blank=True)
    city_address = models.CharField(max_length=60, blank=True)
    postcode_address = models.CharField(max_length=60, blank=True)
    country_address = models.CharField(max_length=60, blank=True)
    fire_department = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Incident(models.Model):
    active = models.BooleanField(default=False)
    message = models.TextField(max_length=200, blank=True)
    address = models.CharField(max_length=40, blank=True)
    pos_lon = models.CharField(max_length=30, blank=True)
    pos_lan = models.CharField(max_length=30, blank=True)
    type = models.CharField(max_length=30, blank=True)
    area = models.CharField(max_length=30, blank=True)
    details = models.CharField(max_length=100, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)


class UnderWay(models.Model):
    incident = models.ForeignKey('Incident', on_delete=models.CASCADE)
    telephone = models.CharField(max_length=30, blank=True)
    time = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)

