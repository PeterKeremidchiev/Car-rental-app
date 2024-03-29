from django.urls import path

from car_rental_app.web.views import search_cars, ContactView
from car_rental_app.web.views import index, AboutTemplateView

urlpatterns = (
    path('', index, name='index'),
    path('search/', search_cars, name='search_cars'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contacts/', ContactView.as_view(), name='contacts'),
)