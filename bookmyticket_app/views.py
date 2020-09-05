from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from bookmyticket.log import get_logger
from bookmyticket_app.models import Movie, City, MovieShow, Seat, SeatReservation
from bookmyticket_app.serializers import MovieSerializer, SeatSerializer, MovieShowCustomSerializer, UserSerializer, \
    BookingSerializer

logger = get_logger(__name__)


class MovieInCityView(ListAPIView):
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            city_name = kwargs.get('name', None)
            logger.info(f"New request for city {city_name}")
            city = City.objects.filter(name=city_name)
            if city:
                city = city[0]
            else:
                logger.warning(f"Incorrect city provided {city_name}")
                return Response({"status": 'failed', 'data': 'invalid city'}, status=400)
            self.queryset = Movie.objects.filter(movieshow__audi__cinema_hall__city__exact=city).distinct()
            serializer = self.get_serializer(self.queryset, many=True)
            logger.info(f"success in getting data for {city_name}")
            return Response({"status": 'success', 'data': serializer.data})
        except Exception as e:
            logger.exception(f"exception in getting data:{e}")
            return Response({"status": 'failed', 'data': 'invalid data'}, status=400)


class MovieiInCinemaPlayingView(ListAPIView):
    serializer_class = MovieShowCustomSerializer

    def get(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            movie_name = kwargs.get('name', None)
            logger.info(f"New request for movie {movie_name}")
            movie = Movie.objects.filter(name__iexact=movie_name)
            if movie:
                movie = movie[0]
            else:
                logger.warning(f"Incorrect movie provided {movie_name}")
                return Response({"status": 'failed', 'data': 'invalid movie'}, status=400)
            self.queryset = MovieShow.objects.prefetch_related().filter(is_playing=True).filter(movie=movie)
            serializer = self.get_serializer(self.queryset, many=True)
            logger.info(f"success in getting data for {movie_name}")
            return Response({"status": 'success', 'data': serializer.data})
        except Exception as e:
            logger.exception(f"exception in getting data:{e}")
            return Response({"status": 'failed', 'data': 'invalid data'}, status=400)


class SeatAvailableForShowView(ListAPIView):
    serializer_class = MovieShowCustomSerializer
    seat_serializer_class = SeatSerializer

    def get(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            logger.info(f"New request for seat status for each show")
            all_shows = MovieShow.objects.select_related()
            resp = list()
            for show in all_shows:
                data = dict()
                serializer = self.get_serializer(show)
                data['show'] = serializer.data
                seats = Seat.objects.exclude(id__in=Seat.objects.filter(seatreservation__booking__movie_show=show))
                seats_data = self.seat_serializer_class(seats, many=True, context={'request': request})
                data['seats_available'] = seats_data.data
                seats = Seat.objects.filter(seatreservation__booking__movie_show=show)
                seats_data = self.seat_serializer_class(seats, many=True, context={'request': request})
                data['seats_occupied'] = seats_data.data
                resp.append(data)
            logger.info(f"success in getting data for seat status for each show")
            return Response({"status": 'success', 'data': resp})
        except Exception as e:
            logger.exception(f"exception in getting data:{e}")
            return Response({"status": 'failed', 'data': 'invalid data'}, status=400)


class UserCreate(APIView):

    def post(self, request, format='json'):
        """

        :param request:
        :param format:
        :return:
        """
        try:
            logger.info("New user creation initiated")
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    logger.info("New user succesfully created")
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.warning("error in creating user")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(f"exception {e}")
            return Response({"status": "failed", "data": "something went wrong"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BookingView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, format=None):
        """

        :param request:
        :param format:
        :return:
        """
        try:
            data = request.data
            data['user'] = request.user.id
            logger.info(f"new booking initated")
            serializer = BookingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                resp = serializer.data
                seat_no = data['seat']
                seat = SeatReservation(seat_id=seat_no, booking_id=resp['id'])
                seat.save()
                logger.info(f"new booking succesful")
                return Response({"status": "success", "booking_id": resp['booking_uuid']},
                                status=status.HTTP_201_CREATED)
            logger.warning(f"issue in new booking")
            return Response({"status": "failed", "data": "incorrect data"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(f"exception {e}")
            return Response({"status": "failed", "data": "something went wrong"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
