from django.urls import path

from car_rental_app.bookings.views import BookingListView, DeleteBookingView, add_review

urlpatterns = (
    path('', BookingListView.as_view(), name='book_list'),
    path('reviews/', add_review, name='add_review'),
    path('bookings/<int:booking_id>/remove/', DeleteBookingView.as_view(), name='book_delete'),
)