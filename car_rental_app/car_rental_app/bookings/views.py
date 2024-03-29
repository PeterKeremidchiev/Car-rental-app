from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from django.shortcuts import render, get_object_or_404, redirect

from car_rental_app.bookings.forms import ReviewForm
from car_rental_app.bookings.models import Booking
from car_rental_app.cars.models import Car


# Create your views here.
class BookingListView(LoginRequiredMixin, views.ListView):
    template_name = 'bookings/bookings.html'
    model = Booking

    def get_queryset(self):

        return Booking.objects.filter(user=self.request.user)

class BookCarView(views.View):
    def get(self, request, *args, **kwargs):
        car_id = self.kwargs.get('pk')
        car = get_object_or_404(Car, pk=car_id)

        if car.available:

            booking = Booking.objects.create(
                user=request.user,
                car=car,
            )

            car.available = False
            car.save()

        return redirect('cars')

class DeleteBookingView(views.View):
    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, id=booking_id)
        car = booking.car

        if booking.user == request.user:
            car.available = True
            car.save()
            booking.delete()

        return redirect('book_list')

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('index')
    else:
        form = ReviewForm()

    context = {
        'form': form
    }
    return render(request, 'bookings/add_review.html', context)