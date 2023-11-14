from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class RegistrationFormView(CreateView):
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = "/accounts/login"
