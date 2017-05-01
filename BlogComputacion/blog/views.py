from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/pages/index.html')

def showAll(request):
    return HttpResponse('Aqui estan todos los Posts')

def showOne(request, id):
    return HttpResponse('se ingreso el id ' + id)
