from django.contrib import admin

# Register your models here.
from .models import AlbumPost
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("article_title", "article_body",)

admin.site.register(Article, ArticleAdmin)
admin.site.register(AlbumPost)