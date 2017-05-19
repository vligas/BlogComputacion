from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from .forms import FormPost, CommentForm
from django.shortcuts import redirect, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.
def index(request):
    return render(request, 'blog/pages/index.html')

class showAll(ListView):
    template_name = 'blog/pages/all_post_detail.html'
    model = Post
    paginate_by = 10
    ordering = ['-id'] # para que ordene de menor a mayor (-) tomando en cuenta la fecha de creacion (created_at)

def showOne(request, id):
    post = get_object_or_404(Post, pk = id)
    if not request.session.has_key('viewed_post_%s' % post.id) :
        post.cont_vist += 1
        request.session['viewed_post_%s' % post.id] = True
        post.save()

    context = {
        'post':post,
        'form':CommentForm
    }
    return render(request, 'blog/pages/detail.html', context)

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
