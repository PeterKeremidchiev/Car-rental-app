from django.urls import path

from car_rental_app.bookings.views import BookingListView, DeleteBookingView

urlpatterns = (
    path('bookings/', BookingListView.as_view(), name='book_list'),
    path('bookings/<int:booking_id>/remove/', DeleteBookingView.as_view(), name='book_delete'),
)