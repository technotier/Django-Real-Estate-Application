from django.contrib import admin
from .models import  Category, Listing

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Category, CategoryAdmin)

class ListingAdmin(admin.ModelAdmin):
    list_display = ["title", "city", "price", "state", "sqft"]
    list_editable = ["city", "price", "state", "sqft"]

admin.site.register(Listing, ListingAdmin)