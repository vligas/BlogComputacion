from .models import Post
from django import forms

class FormPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'cover']
        labels = {
            'title': 'Titulo',
            'text': 'Contenido',
            'cover': 'Imagen de portada',
        }
