from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Seat(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="seats")
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.seat_number} at {self.venue.name}"


class Booking(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.customer_name} for {self.seat}"
