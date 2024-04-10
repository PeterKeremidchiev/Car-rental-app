from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from car_rental_app.cars.forms import CarImageForm
from car_rental_app.cars.mixins import CarFieldsMixin
from car_rental_app.cars.models import Car, CarImages


class CarCreateView(LoginRequiredMixin, UserPassesTestMixin, CarFieldsMixin, views.CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'price_per_day', 'image', 'transmission', 'type_of_fuel', 'fuel_consumption']
    template_name = 'cars/car_create.html'
    success_url = reverse_lazy('cars')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        car = form.save(commit=False)
        car.save()
        return super().form_valid(form)

class CarImageCreateView(views.CreateView):
    model = CarImages
    form_class = CarImageForm
    template_name = 'cars/car_image_create.html'


    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.car.pk})
    def form_valid(self, form):

        return super().form_valid(form)
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



