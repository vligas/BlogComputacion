from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.Register(Post) # registe los Posts para que se vean en el admin panel
