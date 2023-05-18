from .models import Booking
from rest_framework import serializers
from hotel.serializers import HotelSerializer


class BookingCreateSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(source="hotel_id", read_only=True)

    class Meta:
        model = Booking
        fields = ["user_id", "hotel_id",
                  "booking_time", "hotel", "booking_status", "booking_id"]
