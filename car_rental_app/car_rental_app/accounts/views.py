from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout

from django.urls import reverse_lazy, reverse

from django.views import generic as views

from car_rental_app.accounts.forms import CarRentalUserCreationForm
from car_rental_app.accounts.models import CarRentalUser, Profile
from car_rental_app.bookings.models import Booking


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/user-login.html'
    redirect_authenticated_user = True

class RegisterUserView(views.CreateView):
    template_name = 'accounts/user-register.html'
    form_class = CarRentalUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        result = super().form_valid(form)

        login(self.request, form.instance)

        return result

def logout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "accounts/profile-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['bookings'] = Booking.objects.filter(user=user).count()
        return context


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/profile-edit.html"
    fields = ("first_name", "last_name", "profile_picture")

    def get_success_url(self):
        return reverse("profile_details", kwargs={
            "pk": self.object.pk,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["first_name"].initial = self.object.first_name
        form.fields["last_name"].initial = self.object.last_name
        form.fields["profile_picture"].initial = self.object.profile_picture
        form.fields["first_name"].widget.attrs["placeholder"] = "Enter a first name"
        form.fields["last_name"].widget.attrs["placeholder"] = "Enter a last name"
        form.fields["profile_picture"].widget.attrs["placeholder"] = "Enter a profile picture URL"
        return form

class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "accounts/profile_delete.html"
    success_url = reverse_lazy('index')
