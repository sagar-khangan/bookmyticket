from django.contrib import admin
from bookmyticket_app.models import City, CinemaHall, Cinema, Audi, Movie, MovieShow, Seat, Booking, SeatReservation


class CityAdmin(admin.ModelAdmin):
    pass


class CinemaHallAdmin(admin.ModelAdmin):
    pass


class CinemaAdmin(admin.ModelAdmin):
    pass


class AudiAdmin(admin.ModelAdmin):
    pass


class MovieAdmin(admin.ModelAdmin):
    pass


class MovieShowAdmin(admin.ModelAdmin):
    pass


class SeatAdmin(admin.ModelAdmin):
    pass


class BookingAdmin(admin.ModelAdmin):
    pass


class SeatReservationAdmin(admin.ModelAdmin):
    pass


admin.site.register(City, CityAdmin)
admin.site.register(CinemaHall, CinemaHallAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Audi, AudiAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShow, MovieShowAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(SeatReservation, SeatReservationAdmin)
