from django import forms

from car_rental_app.cars.models import Car, CarImages


class CarSearchForm(forms.Form):
    make = forms.CharField(
        max_length=100,
        required=False,
        label='Make',
        widget=forms.TextInput(attrs={'placeholder': 'Enter a make'}))
    model = forms.CharField(
        max_length=100,
        required=False,
        label='Model',
        widget=forms.TextInput(attrs={'placeholder': 'Enter a model'}))
    year = forms.CharField(
        max_length=4,
        required=False,
        label='Year',
        widget=forms.TextInput(attrs={'placeholder': 'Enter a year'}))
    price_per_day = forms.ChoiceField(
        choices=[
        ('', 'range'),
        ('0-50', '$0 - $50'),
        ('51-100', '$51 - $100'),
        ('101-200', '$101 - $200'),
        ('201-1000', '$201 - $1000'),
        ],
        required=False,
        label='Cost per day')


class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImages
        fields = ['image_url', 'car']
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'Enter image URL'}),
            'car': forms.Select(attrs={'placeholder': 'Choose a car'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.all()
        self.fields['car'].empty_label = 'Choose a car'