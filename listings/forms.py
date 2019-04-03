from django import forms
from .models import Listing

class CreatePost(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "realtor",
            "category",
            "title",
            "description",
        ]

