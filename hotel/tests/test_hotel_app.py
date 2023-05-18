from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from hotel.models import Hotel
from hotel.serializers import HotelSerializer

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from hotel.models import Hotel
from hotel.serializers import HotelSerializer


class AllHotelAPITestCase(APITestCase):
    def setUp(self):
        self.hotel = Hotel.objects.create(
            hotel_id=1,
            hotel_name='Test Hotel 1',
            hotel_location='Test Location 1',
            bed_rooms='Test Bed Rooms 1',
            latitude=1.23,
            longitude=4.56,
        )
        self.url = reverse('all_hotels')

    def test_list_all_hotels(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = [HotelSerializer(self.hotel).data]
        self.assertEqual(response.data, expected_data)
