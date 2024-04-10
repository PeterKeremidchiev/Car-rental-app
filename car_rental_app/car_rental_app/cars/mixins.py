class CarFieldsMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['make'].widget.attrs['placeholder'] = 'Enter car make'
        form.fields['model'].widget.attrs['placeholder'] = 'Enter car model'
        form.fields['year'].widget.attrs['placeholder'] = 'Enter car year'
        form.fields['price_per_day'].widget.attrs['placeholder'] = 'Enter car price per day'
        form.fields['image'].widget.attrs['placeholder'] = 'Enter image URL'
        form.fields['transmission'].widget.attrs['placeholder'] = 'Enter the type of car transmission'
        form.fields['type_of_fuel'].widget.attrs['placeholder'] = 'Enter the type of fuel'
        form.fields['fuel_consumption'].widget.attrs['placeholder'] = 'Enter the fuel consumption'
        return form