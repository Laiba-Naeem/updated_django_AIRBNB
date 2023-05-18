from django.shortcuts import get_object_or_404
from django.http import Http404
from Booking.serializers import BookingCreateSerializer
from .models import Booking
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.


class BookingView(APIView):
    permission_classes = (IsAuthenticated,)
    # serializer_class = BookingCreateSerializer

    def post(self, request, *args, **kwargs):
        # user_id = request.GET.get('user_id', None)
        request.data["user_id"] = request.user.id
        request.data["booking_status"] = 1
        serializer = BookingCreateSerializer(data=request.data)
        print("request.data", request.data)
        print("user_id", request.user.id)

        print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        else:
            return Response({"msg": "serialzer not valid"})

    def get(self, request, *args, **kwargs):
        try:
            # user_id = request.GET.get('user_id', None)

            """below line is getting user id from access token"""
            request.data["user_id"] = request.user.id
            # print(user_id)
            instance = Booking.objects.filter(
                user_id=request.data["user_id"], booking_status=1)
            serializer = BookingCreateSerializer(instance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Booking.DoesNotExist:
            return Response(
                {"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND
            )


# class BookingCancellationView(generics.DestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingCreateSerializer

#     def post(self, request):
#         """
#         Perform the booking cancellation logic.
#         """

#         booking_time = request.data["booking_time"]
#         # user_id = request.data["user_id"]
#         request.data["user_id"] = request.user.id
#         # Calculate the check-in time minus 1 day
#         booking_time = datetime.strptime(booking_time, "%Y-%m-%d %H:%M:%S.%f")
#         check_in_time = booking_time - timedelta(days=1)
#         print("allowed time difference\n", check_in_time)
#         now = datetime.now()

        # if now > check_in_time:
        #     print("TRUE")
        #     Booking.objects.filter(user_id=request.data["user_id"]).delete()
        #     print("Booking has been cancelled against the Mentioned User ID ")
        #     return Response(
        #         {
        #             "Cancel Msg": "Booking has been cancelled against the Mentioned User ID "
        #         }
        #     )
        # else:
        #     print("FALSE")

        #     print(
        #         "Booking cancellation is not allowed as the check-in time is less than 1 day away."
        #     )
        #     return Response(
        #         {
        #             "error": "Booking cancellation is not allowed as the check-in time is less than 1 day away."
        #         },
        #         status=status.HTTP_404_NOT_FOUND,
        #     )


# /////////////////////////////////////////////
# ////////////////////////////////////////////
# class BookingCancellationView(generics.DestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingCreateSerializer

#     def post(self, request):
#         """
#         Perform the booking cancellation logic.
#         """

#         booking_time = request.data["booking_time"]

#         print("This is Booking ID....", request.data)
#         request.data["user_id"] = request.user.id
#         # Calculate the check-in time minus 1 day
#         booking_time = datetime.strptime(booking_time, "%Y-%m-%d %H:%M:%S.%f")
#         check_in_time = booking_time - timedelta(days=1)
#         print("allowed time difference\n", check_in_time)
#         now = datetime.now()

#         if now > check_in_time:
#             print("TRUE")
#             bookings = Booking.objects.filter(
#                 user_id=request.data["user_id"], booking_status=1
#             )
#             for booking in bookings:
#                 hotel_id = booking.hotel_id_id
#                 booking.delete()
#                 print(
#                     f"Booking has been cancelled for User ID {request.data['user_id']} and Hotel ID {hotel_id}")
#             return Response(
#                 {
#                     "Cancel Msg": "Booking has been cancelled."
#                 }
#             )
#         else:
#             print("FALSE")
#             print(
#                 "Booking cancellation is not allowed as the check-in time is less than 1 day away."
#             )
#             return Response(
#                 {
#                     "error": "Booking cancellation is not allowed as the check-in time is less than 1 day away."
#                 },
#                 status=status.HTTP_404_NOT_FOUND,
#             )


class BookingCancellationView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer

    def post(self, request):
        """
        Perform the booking cancellation logic.
        """

        booking_id = request.data.get("booking_id")
        if not booking_id:
            return Response(
                {
                    "error": "booking_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            booking = Booking.objects.get(
                booking_id=booking_id, user_id=request.user.id, booking_status=1)
        except Booking.DoesNotExist:
            raise Http404

        booking.booking_status = 0
        booking.save()

        return Response(
            {
                "message": "Booking has been cancelled."
            }
        )
