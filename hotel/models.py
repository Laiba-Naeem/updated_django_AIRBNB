from django.db import models

# Create your models here.
class Hotel(models.Model):
  
    hotel_id = models.IntegerField(primary_key=True)

    hotel_name = models.CharField(max_length=50, null=True, blank=True)
    hotel_location = models.CharField(max_length=50, null=True, blank=True)
    bed_rooms = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()