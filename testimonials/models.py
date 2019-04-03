from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    designation = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

class Partner(models.Model):
    partner_name = models.CharField(max_length=200)
    partner_logo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.partner_name

