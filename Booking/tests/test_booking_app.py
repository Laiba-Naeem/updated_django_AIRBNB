from rest_framework.test import APITestCase
from hotel.models import Hotel
from accounts.models import User
from django.urls import reverse
from rest_framework import status
from Booking.models import Booking


class BookingViewTestCase(APITestCase):
    def setUp(self):
        self.hotel = Hotel.objects.create(
            hotel_id=1, hotel_name="Test Hotel", latitude=37.1234, longitude=-122.5678
        )

        self.user = User.objects.create_user(
            name="testuser", password="testpass", email="test@test.com"
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse("booking")

    def test_create_booking(self):
        data = {
            "hotel_id": self.hotel.hotel_id,
            "user_id": self.user.id,
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.hotel_id, self.hotel)
        self.assertEqual(booking.user_id, self.user)
