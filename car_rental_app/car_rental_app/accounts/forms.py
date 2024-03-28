from django.contrib.auth import forms as auth_forms
from django import forms

from car_rental_app.accounts.models import CarRentalUser, Profile


class CarRentalUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = CarRentalUser
        fields = ('email',)



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "profile_picture")
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter a first name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter a last name"}),
            "profile_picture": forms.URLInput(attrs={"placeholder": "Enter a profile picture URL"}),
        }

class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "profile_picture")

    def __init__(self, *args, **kwargs):
        super(ProfileDeleteForm, self).__init__(*args, **kwargs)
        user_email = self.instance.email
        user = self.instance.profile
        self.fields['email'] = forms.EmailField(label='Email', initial=user_email, disabled=True)
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['profile_picture'].initial = user.profile_picture
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
