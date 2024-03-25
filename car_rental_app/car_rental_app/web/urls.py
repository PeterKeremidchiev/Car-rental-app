from django.urls import path

from car_rental_app.web.views import index, AboutTemplateView, ContactsTemplateView

urlpatterns = (
    path('', index, name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
)