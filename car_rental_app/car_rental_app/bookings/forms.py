from django import forms

from car_rental_app.bookings.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'review': forms.Textarea(attrs={'rows': 6, 'cols': 35}),
        }
        labels = {
            'rating': 'Give us a rating',
            'review': 'Write a review',
        }