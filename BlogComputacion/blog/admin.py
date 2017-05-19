from django.contrib import admin
from .models import Post, Comment, Category
# Register your models here.

admin.site.register(Post) # registe los Posts para que se vean en el admin panel
admin.site.register(Comment)
admin.site.register(Category)
