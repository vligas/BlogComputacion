from django.conf.urls import url
from . import views
from .views import showAll

urlpatterns = [
    url(r'^$', views.index, name='index'),  # Index de la pagina
    url(r'^posts/$',views.showAll, name='showAll'),  # Muestra todos los posts
    url(r'^contact/$', views.contact, name='contact'),  # Muestra todos los posts
    url(r'^posts/(?P<id>[0-9]+)/$', views.showOne, name='showOne'),  # Muestra un post en especifico con todos sus detalles
    url(r'^mis_post/$', views.showAllMyPost, name='showAllMyPost'),
    url(r'^posts/(?P<id>[0-9]+)/edit', views.updatePost, name = 'update'),
    url(r'^create_post/$', views.createPost, name="create"), # en esta url cuando se realiza una peticion GET se muestra el formulario, y cuando es una peticion POST se procesa y se redirecciona en caso de ser correcto
    url(r'^posts/(?P<id>[0-9]+)/borrar', views.deletePost, name ='deletePost'),
    url(r'^enviarSugerencia/', views.enviarSugerencia, name = 'enviarSugerencia'),
    url(r'^posts/(?P<id>[0-9]+)/comentar/', views.addComment, name = "addComment"),
    url(r'^posts/(?P<id>[0-9]+)/eliminar', views.removeComment, name = 'removeComment')
]
