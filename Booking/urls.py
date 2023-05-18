from django.urls import path
from Booking.views import BookingView, BookingCancellationView


urlpatterns = [
    path("booking/", BookingView.as_view(), name="booking"),
    path("bookinghist/", BookingView.as_view(), name="booking_id"),
    path("cancel/", BookingCancellationView.as_view(), name="cancel"),
]
