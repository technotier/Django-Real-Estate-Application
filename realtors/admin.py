from django.contrib import admin
from .models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "designation", "phone"]
    list_editable = ["email", "designation", "phone"]

admin.site.register(Realtor, RealtorAdmin)