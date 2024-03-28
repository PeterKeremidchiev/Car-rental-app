from django.contrib import admin

from car_rental_app.bookings.models import Review


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','review', 'rating', 'date_created')
