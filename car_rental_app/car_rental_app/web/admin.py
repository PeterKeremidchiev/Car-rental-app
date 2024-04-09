from django.contrib import admin

from car_rental_app.web.models import Contact



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'timestamp')
    list_filter = ('phone',)
