from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    # falta autor
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True) # para que se llene automaticamente al instanciar el objeto
    cont_vist = models.IntegerField()

class ImgOfPost(models.Model):
    #img = models.ImageField()
    Post = models.ForeignKey(Post, on_delete = models.CASCADE)
