from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from car_rental_app.accounts.models import Profile

UserModel = get_user_model()
#
#
# @receiver(post_save, sender=UserModel)
# def user_created(sender, instance, created, **kwargs):
#
#     if not created:
#         return
#
#     Profile.objects.create(user=instance)
@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(pre_delete, sender=Profile)
# def delete_user_on_profile_delete(sender, instance, **kwargs):
#
#     instance.user.delete()