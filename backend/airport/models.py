from django.db import models

from backend.account.models import Passenger


class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    airport_plane_capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.code})"


class Plane(models.Model):
    name = models.CharField(max_length=100)
    plane_code = models.CharField(max_length=6)
    capacity = models.IntegerField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.plane_code})"


class Flight(models.Model):
    code = models.CharField(max_length=6)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    starting_time = models.DateTimeField(null=True, blank=True)
    reaching_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.code} ({self.plane})"

    def is_valid_flight(self):
        return self.departure_airport != self.destination_airport and self.starting_time < self.reaching_time


class Ticket(models.Model):
    class TicketTypeChoices(models.TextChoices):
        ECONOMY = "Economy", "Economy"
        BUSINESS = "Business", "Business"
        FIRST = "First", "First"

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TicketTypeChoices.choices)
    price = models.OneToOneField('PriceTicket', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.flight} - {self.type}"


class PriceTicket(models.Model):
    class TicketTypeChoices(models.TextChoices):
        ECONOMY = "Economy", "Economy"
        BUSINESS = "Business", "Business"
        FIRST = "First", "First"

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TicketTypeChoices.choices)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.flight} - {self.type}"
