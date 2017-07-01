from django.db import models
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# NOTE
# como nota general hay algunas cosas que se repiten mucho, las enumerare
# 1) auto_now_add hace que se añada automaticamente al crearse la hora y que posteriormente no pueda ser cambiada
# 2) auto_now hace que se añada automaticamente al editarse o crearse el objeto (lo que quiere decir que cuando se actualiza cambia)
# 3) __str__ es la representacion como cadena, dicha representacion es util para hacer cosas como print(post) o {{ post }} o visualizacion en el admin panel
# 4) related_name se refiere a como acceder a ese campo desde la otra clase ejemplo:
#       post.category
#       category.posts
#
# 5) reverse devuelve la url completa a partir de un nombre y argumentos de alguna url
# 6) on_delete define el comportamiento que ocurre al borrar la una de las partes de la relacion
# 7) blank significa que puede estar vacio (TODO investigar diferencia entre blank=True y null=True)
# NOTE

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    cont_vist = models.IntegerField(default=0)
    cover = models.ImageField()
    category = models.ManyToManyField(Category, related_name='posts', blank=True) # Agregue blank = True ya que no me dejaba crear post ni editarlos sin categorias, y en este momento es imposible crearlos con categorias

    def get_absolute_url(self):
        return reverse("showOne", kwargs={"id":self.id})

    @method_decorator(permission_required('Post.add_Post', reverse_lazy('Post:Post'))) # BUG revisar que es esto, no tengo la menor idea de que hace
    def dispatch(self, *args, **kwargs):
        return super(Post, self).dispatch(*args, **kwargs)

    def __str__(self):
        return self.title



class ImgOfPost(models.Model):
    img = models.ImageField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='images', null=True, blank=True)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True,blank=True, related_name='replies')

    def __str__(self):
        return self.text
