from django.urls import path

from car_rental_app.bookings.views import BookCarView
from car_rental_app.cars.views import CarListView, CarDetailView

urlpatterns = (
    path('', CarListView.as_view(), name='cars'),

    path('<int:pk>/book', BookCarView.as_view(), name='book_car'),
    path('<int:pk>/details', CarDetailView.as_view(), name='car_detail'),
)