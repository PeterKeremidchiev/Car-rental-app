from django import forms

from car_rental_app.cars.models import Car

class CarSearchForm(forms.Form):
    make = forms.CharField(max_length=100, required=False, label='Make')
    model = forms.CharField(max_length=100, required=False, label='Model')
    year = forms.CharField(max_length=4, required=False, label='Year')
    price_per_day = forms.ChoiceField(choices=[
        ('', '----------'),
        ('0-50', '$0 - $50'),
        ('51-100', '$51 - $100'),
        ('101-200', '$101 - $200'),
        ('201-1000', '$201 - $1000'),
    ], required=False, label='Cost per day')

# class CarSearchForm(forms.ModelForm):
#     price_per_day_choices = [
#         ('0-50', '$0 - $50'),
#         ('51-100', '$51 - $100'),
#         ('101-200', '$101 - $200'),
#         ('201-1000', '$201 - $1000'),
#     ]
#
#     price_per_day_select = forms.ChoiceField(choices=price_per_day_choices, required=False)
#
#     class Meta:
#         model = Car
#         fields = ['make', 'model', 'year']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['price_per_day_select'].label = 'Cost per day'
#         self.fields['year'].label = 'Year'
#         self.fields['make'].label = 'Make'
#         self.fields['model'].label = 'Model'