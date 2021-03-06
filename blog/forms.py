from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'content', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'type': "text", 'placeholder': "Title", 'name': "title", 'maxlength': "200", 'required': True, 'id': "id_title"}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'type': "text", 'placeholder': "Slug", 'name': "slug", 'maxlength': "200", 'required': True, 'id': "id_slug"}),
           # 'snippet': forms.TextInput(attrs={'class': 'form-control', 'type': "text", 'placeholder': "Snippet", 'name': "snippet", 'maxlength': "200", 'id': "id_snippet"}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': "Author", 'name': "author", 'required': True, 'id': "id_author"}),
            'content': forms.Textarea(attrs={'rows': "5", 'class': "form-control", 'placeholder': "Content", 'name': "content",  'required': True, 'id': "id_content"}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
         #   'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }