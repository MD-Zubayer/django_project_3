from django import forms
from first_models.models import Post1



class Post1Form(forms.ModelForm):
    class Meta:
        model = Post1
        fields = ['title', 'content']
        