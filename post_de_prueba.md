Soy una de las personas que escucho esta palabra 'Framework' muchas veces antes de conocer su significado, por esto traigo este post para poder aclarar la duda a personas que como yo tuvieron curiosidad.

<br>
<div class="grey-text">/\* Antes de empezar me gustaria aclarar que el desarrollo de este post se centrara en frameworks en desarrollo web, donde se podria decir que he tenido alguna experiencia \*/</div>
<br>

Un framework es simplemente una herramienta (o conjunto de herramientras) que facilitan el desarrollo de aplicaciones, ahora, eso es un concepto bastante general ¿no?. pero, ¿de que manera nos ayudan exactamente?

<br>
#### No reinventes la rueda



los frameworks son especialmente buenos en ayudarnos en "retos y dificultades" que se presentan en casi todos los proyectos, ejemplos de esto seria el manejo de usuarios, sistemas de enrutamientos (como se manejan las direcciones que vienen de las peticiones), comunicacion con la base de datos, entre muchas otras funcionalidades que vienen ya por defecto. Esto lo hace cada uno de manera diferente, pero en general tienen el mismo comportamiento.

<br>
#### Organizacion y mantenimiento



Otro punto fuerte es que ayudan a mantener un codigo organizado y marcan una clara estructura de archivos que debe tener nuestra aplicacion, esto beneficia indudablemente en el desarrollo de cualquier aplicacion ya que es mucho mas facil detectar y diferenciar cada parte de nuestro codigo, por ejemplo, un framework podria tener una carpeta destinada a archivos publicos (assets) que seria todo lo relacionado con el css, javascript e imagenes que requiere nuestra aplicacion, podria existir un archivo unicamente desintado a almacenar los patrones de las rutas validas para neustra aplicacion (si el usuario escribiera pentoncesq.com/abc/ no funcionaria, ya que en nuestro caso dicha url no esta contemplada en nuestros archivos de enrutamiento).
```python
# Archivo: urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^index/$', views.algunaFuncion),
	url(r'^posts/$', views.algunaFuncion1),
	url(r'^posts/all/$', views.algunaFuncion2),
	url(r'^administracion/$', views.algunaFuncion3),
]

'''
Las unicas urls que podria acceder un usuario seria
1. misitio.com/index/
2. misitio.com/posts/
3. misitio.com/posts/all/
4. misitio.com/administracion/

En cada caso la funcion a ejecutar (como se va a procesar la peticion)
esta definida por la funcion (views.algunaFuncion).
'''
```

Esta clara separacion de archivos y carpetas permite que tengamos un codigo que sea mas facil de mantener ¿esto que quiere decir?, que al tener una forma muy clara de hacer las cosas y un camino a seguir, se presta menos a que la gente escriba codigo innentendible (aun se puede, yo lo he hecho <i class="fa fa-smile-o"></i>). Esto es extremadamente importante en proyectos donde no trabajamos solos.

<br>
#### Seguridad



Frameworks en general son herramientas utilizadas por miles de personas que ayudan a su desarrollo encontrando fallos y reportandolos, esto hace que sea codigo extremadamente testeado, es mucho menos probable que encuentres un problema con algun error o de seguridad en un framework que en una aplicacion desarrollada por ti.
