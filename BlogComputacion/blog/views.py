from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from .forms import FormPost, CommentForm
from .models import Post, Comment, Category
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q #necesario para la busqueda
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
import operator


#----------| Index de la pagina |----------
def index(request):
    category = Category.objects.all()
    category_show = [
        category[0],
        category[1],
        category[2],
        category[3],
        category[4],
        category[5],
        category[6],
    ]
    posts = Post.objects.all()
    lon = len(posts)
    posts_order = sorted(posts, key=operator.attrgetter('cont_vist'))
    posts_populares = [
        posts[lon-1],
        posts[lon-2],
        posts[lon-3]
    ]
    posts_nuevos = [posts[lon-1], posts[lon-2], posts[lon-3], posts[lon-4]]

    category_populares = []

    for x in posts_populares:
        for y in x.category.all():
            if not y in category_populares:
                category_populares.append(y)

    print(category_populares)
    context = {
        'category':category,
        'category_show':category_show,
        'category_populares':category_populares,
        'posts_populares':posts_populares,
        'posts_nuevos':posts_nuevos

    }
    return render(request, 'blog/pages/index.html', context)
#----------| Busqueda de Posts |------------
def search(request):
    temp = request.GET.get('q','')
    Posts = Post.objects.filter(title__icontains=temp)
    return render(request, 'blog/pages/search.html', {'Posts': Posts})

def search_category(request):
    temp = request.GET.get('category','')
    if temp == 'all':
        return redirect('showAll')
    else:
        posts = Post.objects.filter(category__name=temp)
        category = Category.objects.all()
        context = {
            'posts':posts,
            'category':category
        }
        return render(request,'blog/pages/all_post_detail.html',context)

#--------| views que faltan definir |--------
def contact(request):
    return HttpResponse('contact form')




#------------| CRUD DE LOS POSTS |------------


#-----------| CREATE |-----------
@login_required
@permission_required('blog.add_post', raise_exception=True)
def createPost(request):
    form = FormPost()

    if request.method == "POST":
        form = FormPost(request.POST ,request.FILES)

        if form.is_valid():

            post = form.save(commit=False) # el commit False hace que se cree la instancia pero que no se salve en la base de datos
            post.author = request.user
            post.save()
            return redirect('showOne', id=post.id)

    # en caso de no ser POST, simplemente se devuelve el contextoy se renderiza, (esto quiere decir que se esta intentando acceder para empezara  crear el post, no para guardarlo)
    context = {
    'form':form,
    }

    return render(request, 'blog/pages/crear_post.html', context)



#-------------| READ |-------------
def showAll(request):
    posts_list = Post.objects.all()
    page=request.GET.get('page', 1)
    category = Category.objects.all()

    paginator = Paginator(posts_list,10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts':posts,
        'category':category
    }
    return render(request,'blog/pages/all_post_detail.html',context)

    # paginate_by = 10 # numero de elementos por pagina
    # ordering = ['-id'] # para que ordene de menor a mayor (-) tomando en cuenta el id



def showOne(request, id):

    post = get_object_or_404(Post, pk = id)

    if not request.session.has_key('viewed_post_%s' % post.id) : # se pregunta si existe una cookie llamada viewed_post_id
        # en caso de ser asi se suma uno a las vistas del post y se coloca la cookie para no contar 2 veces la misma persona
        post.cont_vist += 1
        request.session['viewed_post_%s' % post.id] = True
        post.save()

    context = {
        'post':post,
        'form':CommentForm
    }

    return render(request, 'blog/pages/detail.html', context)

@login_required
@permission_required('blog.add_post', raise_exception=True)
def showAllMyPost(request):
    all_post = Post.objects.filter(author = request.user)

    context = {
        'all_post':all_post
    }
    return render(request, 'blog/pages/all_my_post.html', context)

# -----------| UPDATE |-----------
@login_required
@permission_required('blog.add_post', raise_exception=True) # manda un error 403 en caso de personas sin acceso intentando entrar a esta view
def updatePost(request, id):

    instance = get_object_or_404(Post, pk=id)

    if instance.author == request.user: # se verifica que el usuario actual sea el mismo que creo el post

        form = FormPost(request.POST or None, request.FILES or None, instance = instance)

        if( request.method == "POST"): # si es POST quiere decir que se esta actualizando el post
            if form.is_valid():

                instance = form.save()
                return redirect(instance) # esto funciona ya que si a redirect() se le pasa un objeto este llama a su metodo get_absolute_url

        # en caso de ser GET significa que el usuario esta solicitando el formulario para actualizar el post
        context = {
            "title": instance.title,
            "instance": instance,
            "form": form,
        }

        return render(request, 'blog/pages/crear_post.html', context)
    else:
        # en caso de que no sea el usuario que solicito redireccionarlo a la vista detail del post
        return redirect(instance)


# -----------| DELETE VIEW|------------

@login_required
@permission_required('blog.add_post', raise_exception=True)
def deletePost(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('showAllMyPost')


# ---------| VIEW PARA ENVIAR SUGERENCIAS |---------
def enviarSugerencia(request):
    if request.method == "POST" :

        if len(request.POST['mensaje']) != 0 :
            message = request.POST['mensaje']

            if request.user.is_authenticated :
                message = message + "<br>" + "Sugerencia hecha por: " + request.user.username

            send_mail('Sugerencias', 'Una nueva sugerencia', 'probandoelblogcomp@gmail.com', ['probandoelblogcomp@gmail.com'], html_message = message)
        return  redirect('/')
    else:
        return Http404("Page not found")





#-----------| VIEWS PARA LOS COMENTARIOS |-----------

@login_required
def addComment(request, id):
    post = get_object_or_404(Post, pk=id)
    form_comment = CommentForm()

    if request.method == 'POST':
        form_comment = CommentForm(request.POST)

        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    return redirect('showOne', id=post.id)



@login_required
def removeComment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    aux = comment.post.id
    comment.delete()
    return redirect('showOne', id=aux)
