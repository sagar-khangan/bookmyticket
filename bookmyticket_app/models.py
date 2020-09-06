import uuid

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


BOOKING_STATUS = [
    ("BOOKED", "BOOKED"),
    ("PENDING", "PENDING"),
    ("CANCEL", "CANCEL")
]


class City(models.Model):
    name = models.CharField(max_length=1024)
    state = models.CharField(max_length=1024)
    country = models.CharField(max_length=1024)
    pin = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Cinema(models.Model):
    name = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class CinemaHall(models.Model):
    name = models.CharField(max_length=1024)
    cinema = models.ForeignKey(to=Cinema, on_delete=models.CASCADE)
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Audi(models.Model):
    name = models.CharField(max_length=32)
    cinema_hall = models.ForeignKey(to=CinemaHall, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.cinema_hall.name}-{self.cinema_hall.city.name}"

    def __repr__(self):
        return f"{self.name}-{self.cinema_hall.name}-{self.cinema_hall.city.name}"


class Movie(models.Model):
    name = models.CharField(max_length=1024)
    director = models.CharField(max_length=1024)
    cast = models.CharField(max_length=4096)
    release_date = models.DateTimeField()
    duration = models.FloatField()
    description = models.CharField(max_length=4096, null=True, blank=True)
    rating = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class MovieShow(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE)
    audi = models.ForeignKey(to=Audi, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    price = models.FloatField(default=0)
    is_playing = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie.name}-{self.show_time}"

    def __repr__(self):
        return f"{self.movie.name}-{self.show_time}"


class Seat(models.Model):
    row = models.PositiveIntegerField()
    seat_no = models.PositiveIntegerField()
    audi = models.ForeignKey(to=Audi, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.audi}-{self.row}-{self.seat_no}"

    def __repr__(self):
        return f"{self.audi}-{self.row}-{self.seat_no}"
        return f"{self.audi}-{self.row}-{self.seat_no}"


class Booking(models.Model):
    movie_show = models.ForeignKey(to=MovieShow, on_delete=models.CASCADE)
    booking_uuid = models.UUIDField(default=uuid.uuid4(), unique=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booked = models.BooleanField(default=True)
    status = models.CharField(choices=BOOKING_STATUS, null=True, blank=True, max_length=128, default="BOOKED")
    paid = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    amount = models.FloatField(default=0)
    seat_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie_show.movie.name}-{self.movie_show.show_time}"

    def __repr__(self):
        return f"{self.movie_show.movie.name}-{self.movie_show.show_time}"


class SeatReservation(models.Model):
    booking = models.ForeignKey(to=Booking, on_delete=models.CASCADE)
    seat = models.ForeignKey(to=Seat, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.booking.id}"

    def __repr__(self):
        return f"{self.booking.id}"
