# blog/admin.py
from django.contrib import admin
from .models import Post
from .models import Category, Article
from .models import QuillPost
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(Category,  CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass
