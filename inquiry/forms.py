from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            "listing",
            "listing_id",
            "name",
            "email",
            "message",
            "contact_date",
            "user_id"
        ]

