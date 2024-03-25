from django.urls import path

from car_rental_app.bookings.views import BookCarView
from car_rental_app.cars.views import CarListView, CarList2View, search_cars

urlpatterns = (
    path('', CarList2View.as_view(), name='cars'),
    path('search/', search_cars, name='search_cars'),
    path('<int:pk>/book', BookCarView.as_view(), name='book_car'),

)