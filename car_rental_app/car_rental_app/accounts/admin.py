from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()
# Register your models here.
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('email', )

