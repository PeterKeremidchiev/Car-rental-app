from django.shortcuts import render
from django.views import generic as views

from car_rental_app.cars.models import Car


# Create your views here.
# class IndexView(views.ListView):
#     template_name = 'web/index.html'

def index(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'web/index.html', context)

class AboutTemplateView(views.TemplateView):
    template_name = 'web/about.html'

class ContactsTemplateView(views.TemplateView):
    template_name = 'web/contacts.html'