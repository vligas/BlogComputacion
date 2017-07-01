from .models import Post, Comment
from django import forms
#from pagedown.widgets import PagedownWidget

class FormPost(forms.ModelForm):

    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Post
        fields = ['title', 'text', 'cover', 'category']
        labels = {
            'title': 'Titulo',
            'text': 'Contenido',
            'cover': 'Imagen de portada',
            'category':'Agrega categorias'
        }
        # widgets = {
        #     'text': PagedownWidget
        # }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text':'Escribe aqui tu comentario'
        }
