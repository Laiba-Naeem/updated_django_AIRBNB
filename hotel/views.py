from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from rest_framework import generics
from .serializers import HotelSerializer


class FavoriteHotelAPIView(APIView):

    def post(self, request):
        try:
            hotel_id = request.data["hotel_id"]
            print(hotel_id)
            hotel = Hotel.objects.get(hotel_id=hotel_id)
            if hotel:
                return Response(data={"msg": "Hotel Added to fav"})

        except Exception as e:
            return Response(data={"msg": "Hotel does not exists"}, status=status.HTTP_400_BAD_REQUEST)


class AllHotelAPI(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
