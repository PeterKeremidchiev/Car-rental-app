from django.shortcuts import render
from django.views import generic as views

from car_rental_app.cars.models import Car


# Create your views here.
class CarListView(views.ListView):
    queryset = Car.objects.all()
    template_name = 'cars/car_list.html'

class CarList2View(views.ListView):
    queryset = Car.objects.all()
    template_name = 'cars/car_list_2.html'

def search_cars(request):
    make = request.GET.get('make')
    model = request.GET.get('model')
    cost_range = request.GET.get('price_per_day')
    year = request.GET.get('year')
    cars = Car.objects.filter(available=True)


    if make:
        cars = cars.filter(make__icontains=make.lower())
    if model:
        cars = cars.filter(model__icontains=model.lower())
    if year:
        cars = cars.filter(year=year)
    if cost_range:
        min_cost, max_cost = cost_range.split('-')
        cars = cars.filter(price_per_day__range=(min_cost, max_cost))

    return render(request, 'cars/searched_cars_results.html', {'cars': cars})
