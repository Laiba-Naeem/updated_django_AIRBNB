from rest_framework.routers import DefaultRouter
from django.urls import path
from hotel.views import FavoriteHotelAPIView, AllHotelAPI
urlpatterns = [
    path('fav/', FavoriteHotelAPIView.as_view(), name='fav_hotel'),
    path('allhotels/', AllHotelAPI.as_view(), name='all_hotels'),
]
