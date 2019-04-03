from django.db import models

# Create your models here.
class Realtor(models.Model):
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d/')
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    fb_link = models.URLField()
    insta_link = models.URLField()
    twitter_link = models.URLField()

    def __str__(self):
        return self.name

