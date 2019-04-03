from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

class editProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

