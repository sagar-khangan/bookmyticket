from rest_framework.authtoken import views as rest_framework_views
from django.urls import path
from bookmyticket_app.views import MovieInCityView,MovieiInCinemaPlayingView,\
    SeatAvailableForShowView,UserCreate,BookingView,Health

urlpatterns = [
    path('health/', Health.as_view(),name='health'),
    path('city/<str:name>/movie/', MovieInCityView.as_view()),
    path('cinemahall/movie/<str:name>/', MovieiInCinemaPlayingView.as_view()),
    path('show/seat/', SeatAvailableForShowView.as_view()),
    path('auth/signup/', UserCreate.as_view(),name='signup'),
    path('auth/login/', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    path('movie/book/', BookingView.as_view(),name='book_movie'),

]

