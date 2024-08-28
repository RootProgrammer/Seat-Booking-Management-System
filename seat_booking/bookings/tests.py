from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Venue, Seat, Booking


class BookingSystemTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.venue = Venue.objects.create(name="Test Venue", location="Test Location")
        self.seat1 = Seat.objects.create(venue=self.venue, seat_number="A1")
        self.seat2 = Seat.objects.create(venue=self.venue, seat_number="A2")

    def test_create_venue(self):
        response = self.client.post(
            "/api/venues/", {"name": "New Venue", "location": "New Location"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Venue.objects.count(), 2)

    def test_create_seat(self):
        response = self.client.post(
            "/api/seats/", {"venue": self.venue.id, "seat_number": "B1"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Seat.objects.count(), 3)

    def test_create_booking(self):
        response = self.client.post(
            "/api/bookings/", {"seat": self.seat1.id, "customer_name": "John Doe"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_double_booking(self):
        # First booking should succeed
        self.client.post(
            "/api/bookings/", {"seat": self.seat1.id, "customer_name": "John Doe"}
        )
        # Second booking for the same seat should fail
        response = self.client.post(
            "/api/bookings/", {"seat": self.seat1.id, "customer_name": "Jane Doe"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
