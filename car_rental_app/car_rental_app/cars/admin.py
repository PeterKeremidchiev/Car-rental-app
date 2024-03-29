from django.contrib import admin

from car_rental_app.cars.models import Car, CarImages


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'year', 'price_per_day', 'fuel_consumption', 'transmission', 'available', 'booked_by',)
    list_filter = ('available', 'make', 'fuel_consumption', 'transmission')

@admin.register(CarImages)
class CarImagesAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'car')
    list_filter = ('car',)

