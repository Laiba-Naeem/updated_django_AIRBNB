from django.db import models
from hotel.models import Hotel
from accounts.models import User


# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, editable=False)
    hotel_id = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="hotelid"
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="userid")
    booking_time = models.DateTimeField(null=True)
    check_out_time = models.DateTimeField(auto_now_add=True)
    booking_status = models.IntegerField(default=0)
