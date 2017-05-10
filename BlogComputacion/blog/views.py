from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'blog/pages/index.html')

def showAll(request):
    return HttpResponse('Aqui estan todos los Posts')

def showOne(request, id):
    return HttpResponse('se ingreso el id ' + id)


def contact(request):
    return HttpResponse('contact form')

def enviarSugerencia(request):
    send_mail('Sugerencias', 'Una nueva sugerencia', 'probandoelblogcomp@gmail.com', ['probandoelblogcomp@gmail.com'], html_message = request.POST['mensaje'])
    return  redirect('/')
