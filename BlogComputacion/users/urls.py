from django.conf.urls import url
from .views import UserRegister

urlpatterns = [
    url(r'^registrar/', UserRegister.as_view(), name = "registrar")
]
