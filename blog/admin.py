from django.contrib import admin
from .models import Author, Article

# Register your models here.
admin.site.register(Author)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "posted_on", "updated_on", "article_author"]
    list_display_links = ["title", "posted_on", "updated_on", "article_author"]

admin.site.register(Article, ArticleAdmin)