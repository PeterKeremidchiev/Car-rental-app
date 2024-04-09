from django.shortcuts import render
from django.views import generic as views

from car_rental_app.cars.forms import CarSearchForm
from car_rental_app.cars.models import Car


# Create your views here.
class CarListView(views.ListView):
    queryset = Car.objects.all()
    template_name = 'cars/car_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        context['available_cars'] = Car.objects.filter(available=True)
        return context

class CarDetailView(views.DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        context['image_urls'] = [image.image_url for image in car.images.all()]
        return context



