from rest_framework import viewsets, serializers
from .models import Venue, Seat, Booking
from .serializers import VenueSerializer, SeatSerializer, BookingSerializer


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        seat = serializer.validated_data["seat"]
        if Booking.objects.filter(seat=seat).exists():
            raise serializers.ValidationError("This seat is already booked.")
        serializer.save()
