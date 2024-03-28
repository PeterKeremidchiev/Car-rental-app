from django import forms

from car_rental_app.web.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control', 'id': 'inputName4'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'inputEmail4'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control', 'id': 'inputSubject4'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control', 'id': 'inputMessage'}),
        }