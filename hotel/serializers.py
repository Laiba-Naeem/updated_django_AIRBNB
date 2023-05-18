
from rest_framework import serializers
from .models import Hotel
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_id', 'hotel_name', 'hotel_location', 'bed_rooms', 'latitude', 'longitude']