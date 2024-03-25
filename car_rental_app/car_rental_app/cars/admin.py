from django.contrib import admin

from car_rental_app.cars.models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price_per_day', 'available', 'booked_by',)
    list_filter = ('available', )
