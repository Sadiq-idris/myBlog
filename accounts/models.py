from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile images", default="default.jpg")
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

    def get_absolute_url(self):
        return reverse("home")