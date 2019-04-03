from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('article/<int:blog_id>', views.single_blog, name='single_blog'),
]

