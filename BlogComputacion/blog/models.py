from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    # falta autor
    date = models.DateField()
    cont_vist = models.IntegerField()

class ImgOfPost(models.Model):
    #img = models.ImageField()
    Post = models.ForeignKey(Post, on_delete = models.CASCADE)
