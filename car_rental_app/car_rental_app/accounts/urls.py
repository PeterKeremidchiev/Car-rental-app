from django.urls import path, include

from car_rental_app.accounts.views import LoginUserView, RegisterUserView, logout_user, ProfileDetailsView, \
    ProfileUpdateView, ProfileDeleteView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path(
        "profile/<int:pk>/", include([
            path("", ProfileDetailsView.as_view(), name="profile_details"),
            path("edit/", ProfileUpdateView.as_view(), name="profile_edit"),
            path("delete/", ProfileDeleteView.as_view(), name="profile_delete"),
        ]),
    )
)