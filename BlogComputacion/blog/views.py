from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from .forms import FormPost
from django.shortcuts import redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.
def index(request):
    return render(request, 'blog/pages/index.html')

class showAll(ListView):
    template_name = 'blog/pages/all_post_detail.html'
    model = Post
    paginate_by = 5
    ordering = ['-id'] # para que ordene de menor a mayor (-) tomando en cuenta la fecha de creacion (created_at)

def showOne(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'blog/pages/detail.html', {'post':post})

def contact(request):
    return HttpResponse('contact form')

@login_required
@permission_required('blog.add_post', raise_exception=True)
def createPost(request):
    form = FormPost()

    if request.method == "POST":
        form = FormPost(request.POST ,request.FILES)

        if form.is_valid():
            post = form.save(commit=False) # aqui era form.save..... deje el post = form.save() para poder hacer post.pk despues
            post.author = request.user
            post.save()
            return redirect('showOne', id=post.id) # aqui era id, no pk

    return render(request, 'blog/pages/crear_post.html', {'form':form}) # aqui modifique la direccion del template y lo meti dentro de la carpeta pages


@login_required
@permission_required('blog.add_post', raise_exception=True)
def updatePost(request, id):
    instance = get_object_or_404(Post, pk=id)
    if instance.author == request.user :
        form = FormPost(request.POST or None, request.FILES or None, instance = instance)

        if( request.method == "POST"):
            if form.is_valid():
                instance = form.save() # aqui era form.save..... deje el post = form.save() para poder hacer post.pk despues
                return redirect(instance)

        context = {
            "title": instance.title,
            "instance": instance,
            "form": form,
        }
        return render(request, 'blog/pages/crear_post.html', context)
    else:
        return redirect('showOne', id=instance.id)

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
