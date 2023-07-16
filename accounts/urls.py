from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.SignUp.as_view(), name="signup"),
    path("profile", views.profile, name="profile"),
    path("profile-update/<int:pk>", views.ProfileUpdate.as_view(), name="profile_update"),
]