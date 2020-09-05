from django.db import models

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


class Cinema(models.Model):
    name = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CinemaHall(models.Model):
    name = models.CharField(max_length=1024)
    cinema = models.ForeignKey(to=Cinema, on_delete=models.CASCADE)
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Audi(models.Model):
    name = models.CharField(max_length=32)
    cinema_hall = models.ForeignKey(to=CinemaHall, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


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


class MovieShow(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE)
    audi = models.ForeignKey(to=Audi, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Seat(models.Model):
    row = models.PositiveIntegerField()
    seat_no = models.PositiveIntegerField()
    audi = models.ForeignKey(to=Audi, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    movie_show = models.ForeignKey(to=MovieShow, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)
    status = models.CharField(choices=BOOKING_STATUS, null=True, blank=True,max_length=128)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    seat_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SeatReservation(models.Model):
    booking = models.ForeignKey(to=Booking, on_delete=models.CASCADE)
    seat = models.ForeignKey(to=Seat, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

