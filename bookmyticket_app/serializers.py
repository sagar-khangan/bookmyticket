from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from bookmyticket_app.models import City, CinemaHall, Cinema, Audi, Movie, MovieShow, Seat, SeatReservation, Booking


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'state', 'country')


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('name',)


class AudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audi
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieShow
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class SeatReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatReservation
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class MovieCustomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'director', 'cast', 'duration', 'description', 'rating')


class CinemaHallCustomSerializer(serializers.HyperlinkedModelSerializer):
    cinema = CinemaSerializer()
    city = CitySerializer()

    class Meta:
        model = CinemaHall
        fields = ('name', 'cinema', 'city')


class AudiCustomSerializer(serializers.HyperlinkedModelSerializer):
    cinema_hall = CinemaHallCustomSerializer()

    class Meta:
        model = Audi
        fields = ('name', 'cinema_hall')


class MovieShowCustomSerializer(serializers.HyperlinkedModelSerializer):
    movie = MovieCustomSerializer()
    audi = AudiCustomSerializer()

    class Meta:
        model = MovieShow
        fields = ('movie', 'show_time', 'price', 'is_playing', 'audi')


class SeatCustomSerializer(serializers.HyperlinkedModelSerializer):
    audi = AudiCustomSerializer

    class Meta:
        model = Seat
        fields = ('row', 'seat_no', 'audi')


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class BookingCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
