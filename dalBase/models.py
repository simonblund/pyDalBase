from django.db import models

# Extend the user model
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    vacancy = models.CharField(max_length=30)
    competences = models.CharField(max_length=30, blank=True)
    driverslicence = models.CharField(max_length=30, blank=True)
    primary_phone = models.CharField(max_length=30, unique=True)
    secondary_phone = models.CharField(max_length=30, blank=True)
    telegram_id = models.CharField(max_length=60, blank=True)
    street_address = models.CharField(max_length=60, blank=True)
    city_address = models.CharField(max_length=60, blank=True)
    postcode_address = models.CharField(max_length=60, blank=True)
    country_address = models.CharField(max_length=60, blank=True)
    fire_department = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{} by {}'.format(self.first_name, self.primary_phone)


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

    def __str__(self):
        return '{} by {}'.format(self.address, self.created_at)


class UnderWay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    incident = models.ForeignKey(Incident, null=True)
    telephone = models.ForeignKey(User, to_field="primary_phone")
    time = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return '{} buy {}'.format(self.telephone.vacancy, self.created_at)


class IncidentType(models.Model):
    incident_type = models.CharField(max_length=40)

    def __str__(self):
        return '{} incident_type'.format(self.incident_type)


class IncidentArea(models.Model):
    incident_area_no = models.IntegerField(unique=True)
    incident_area_name = models.CharField(max_length=50)

    def __str__(self):
        return '{} incident_area {}'.format(self.incident_area_name, self.incident_area_no)


class IncidentCause(models.Model):
    incident_cause = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return '{}'.format(self.incident_cause)


class IncidentReport(models.Model):
    incident_id = models.ForeignKey(Incident)
    incident_type = models.ForeignKey(IncidentType)
    incident_type_of_alarm = models.CharField(max_length=30, blank=True)
    incident_message = models.TextField(max_length=400)
    incident_address = models.CharField(max_length=50)
    incident_area = models.ForeignKey(IncidentArea, null=True)
    incident_city = models.CharField(max_length=50)
    incident_detail = models.TextField(max_length=800, blank=True)
    description = models.TextField(max_length=800, blank=True)
    confirmed_fire = models.BooleanField()
    action_taken = models.BooleanField()
    incident_cause = models.ForeignKey(IncidentCause)
    users_on_incident = models.ManyToManyField(User)
    active_users = models.IntegerField(blank=True)
    start_time_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(User, related_name='author')
    image_1 = models.ImageField(upload_to='incident/%Y/%m/%d', blank=True)
    image_2 = models.ImageField(upload_to='incident/%Y/%m/%d', blank=True)
    image_3 = models.ImageField(upload_to='incident/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=False, auto_created=False, blank=True)

    def __str__(self):
        return '{} IR {}'.format(self.incident_id, self.created_at)


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=10)
    vehicle_registration = models.CharField(max_length=10, blank=True)
    vehicle_phone = models.CharField(max_length=20, blank=True)
    vehicle_tetra = models.CharField(max_length=20, blank=True)
    vehicle_description = models.TextField(blank=True)
    vehicle_seats = models.IntegerField(blank=True)
    vehicle_driverslicence = models.CharField(blank=True, max_length=10)

    def __str__(self):
        return '{} buy {}'.format(self.vehicle_name, self.vehicle_registration)


class VehicleUnderWay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_id = models.ForeignKey(Vehicle)
    incident_id = models.ForeignKey(Incident)
    leader = models.ForeignKey(User, related_name='leader')
    km = models.IntegerField(blank=True)
    lon_position = models.FloatField(blank=True, null=True)
    lan_position = models.FloatField(blank=True, null=True)
    underway = models.DateTimeField(blank=True, null=True)
    at_scene = models.DateTimeField(blank=True, null=True)
    free = models.DateTimeField(blank=True, null=True)
    at_base = models.DateTimeField(blank=True, null=True)
    users_in_vehicle = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return '{} buy {}'.format(self.vehicle_id, self.created_at)


class SoftwareNews(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    priority = models.IntegerField()
    show_on_login = models.BooleanField(default=False)
    alert = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return '{} SoftwareNews {}'.format(self.text, self.created_at)