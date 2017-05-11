from django.conf.urls import url
from . import views
from .views import showAll

urlpatterns = [
    url(r'^$', views.index, name='index'),  # Index de la pagina
    url(r'^posts/$', showAll.as_view(), name='showAll'),  # Muestra todos los posts
    url(r'^contact/$', views.contact, name='contact'),  # Muestra todos los posts
    url(r'^posts/(?P<id>[0-9]+)/$', views.showOne, name='showOne'),  # Muestra un post en especifico con todos sus detalles
    url(r'^posts/(?P<id>[0-9]+)/edit', views.updatePost, name = 'update'), 
    url(r'^create_post/$', views.createPost, name="create"), # en esta url cuando se realiza una peticion GET se muestra el formulario, y cuando es una peticion POST se procesa y se redirecciona en caso de ser correcto
    url(r'^enviarSugerencia/', views.enviarSugerencia, name = 'enviarSugerencia')
]
