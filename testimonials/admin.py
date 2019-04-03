from django.contrib import admin
from .models import Testimonial, Partner

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["name", "designation"]

admin.site.register(Testimonial, TestimonialAdmin)

class PartnerAdmin(admin.ModelAdmin):
    list_display = ["partner_name"]

admin.site.register(Partner, PartnerAdmin)