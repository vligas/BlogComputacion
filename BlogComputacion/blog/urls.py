from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  # Index de la pagina
    url(r'^posts/$', views.showAll, name='showAll'),  # Muestra todos los posts
    url(r'^contact/$', views.contact, name='contact'),  # Muestra todos los posts
    url(r'^posts/(?P<id>[0-9]+)$', views.showOne, name='showOne')  # Muestra un post en especifico con todos sus detalles
]
