from django.contrib import admin

from car_rental_app.bookings.models import Review, Booking


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','review', 'rating', 'date_created')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car',)

    def save_model(self, request, obj, form, change):

        super().save_model(request, obj, form, change)

        obj.car.available = False
        obj.car.save()


