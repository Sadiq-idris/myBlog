from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    extra_context = {
        "title":"SignUp",
    }

    template_name = "registration/signup.html"


def profile(request):
    if request.user.is_authenticated:
        title = "Profile-page"
        profile = Profile.objects.get(user=request.user)

        return render(request, "profile.html",{"title":title,"profile":profile})
    
    return HttpResponseRedirect("/")


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    extra_context = {
        "title":"Update profile"
    }
    model = Profile
    login_url = "login"
    success_url = reverse_lazy("profile")
    fields = ['first_name','last_name','profile_image']
    template_name = "profile_update.html"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)