from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic.edit import FormView

from car_rental_app.bookings.models import Review
from car_rental_app.cars.forms import CarSearchForm
from car_rental_app.cars.models import Car
from car_rental_app.web.forms import ContactForm


# Create your views here.
# class IndexView(views.ListView):
#     template_name = 'web/index.html'

def index(request):
    cars = Car.objects.all()
    form = CarSearchForm()
    context = {
        'cars': cars,
        'reviews': Review.objects.all(),
        'form': form,

    }
    return render(request, 'web/index.html', context)

class AboutTemplateView(views.TemplateView):
    template_name = 'web/about.html'


class ContactView(FormView):
    template_name = 'web/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def search_cars(request):
    form = CarSearchForm(request.GET)
    cars = Car.objects.filter(available=True)

    if form.is_valid():
        make = form.cleaned_data.get('make')
        model = form.cleaned_data.get('model')
        year = form.cleaned_data.get('year')
        cost_range = form.cleaned_data.get('price_per_day')

        if make:
            cars = cars.filter(make__icontains=make.lower())
        if model:
            cars = cars.filter(model__icontains=model.lower())
        if year:
            cars = cars.filter(year=year)
        if cost_range:
            min_cost, max_cost = cost_range.split('-')
            cars = cars.filter(price_per_day__range=(min_cost, max_cost))

    return render(request, 'cars/searched_cars_results.html', {'cars': cars, 'form': form})
