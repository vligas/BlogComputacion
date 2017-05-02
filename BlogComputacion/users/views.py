from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
#from django.core.urlresolvers import reverser_lazy
from .forms import RegisterForm

class UserRegister(CreateView):
    model = User
    template_name = "users/register.html"
    form_class = RegisterForm
    #success_url = reverser_lazy() Esto es para la pag a la que se dirige luego de registrar
