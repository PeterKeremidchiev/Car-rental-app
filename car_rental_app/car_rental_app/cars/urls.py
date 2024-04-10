from django.urls import path, include

from car_rental_app.bookings.views import BookCarView
from car_rental_app.cars.views import CarListView, CarDetailView, CarCreateView, CarImageCreateView

urlpatterns = (
    path('', CarListView.as_view(), name='cars'),
    path('create/', CarCreateView.as_view(), name='car_create'),
    path('add_image/', CarImageCreateView.as_view(), name='car_image_create'),
    path('<int:pk>/', include([
        path('book/', BookCarView.as_view(), name='book_car'),
        path('details/', CarDetailView.as_view(), name='car_detail'),
        ]),
    ),
)