from django.db import models
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True) # para que se llene automaticamente al instanciar el objeto
    cont_vist = models.IntegerField(default=0)
    cover = models.ImageField()

    def get_absolute_url(self):
        return reverse("showOne", kwargs={"id":self.id})   # blog:showOne es invalido ya que no tenemos un "namespace" llamado blog

    @method_decorator(permission_required('Post.add_Post', reverse_lazy('Post:Post')))
    def dispatch(self, *args, **kwargs):
        return super(Post, self).dispatch(*args, **kwargs)

class ImgOfPost(models.Model):
    img = models.ImageField()
    Post = models.ForeignKey(Post, on_delete = models.CASCADE)
