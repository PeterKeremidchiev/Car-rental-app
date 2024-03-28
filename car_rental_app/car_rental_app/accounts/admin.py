from django.contrib import admin
from django.contrib.auth import get_user_model

from car_rental_app.accounts.models import Profile

UserModel = get_user_model()
# Register your models here.
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('email', )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'profile_picture', )

