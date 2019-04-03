from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    profile_pic = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name.username

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    blog_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    article_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

