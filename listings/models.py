from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    cat_img = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    ac = models.CharField(max_length=200)
    heater = models.CharField(max_length=200)
    city_views = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    internet = models.CharField(max_length=200)
    laundry = models.CharField(max_length=200)
    metro = models.CharField(max_length=200)
    electric = models.CharField(max_length=200)
    is_publish = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_featured = models.BooleanField(default=False)
    sale_type = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


    def __str__(self):
        return self.title