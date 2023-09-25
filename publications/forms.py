from django import forms
from .models import Post, Tag


class PostForm(forms.ModelForm):
    """
    Форма добавления статей на сайте
    """

    class Meta:
        model = Post
        fields = (
            'name',
            'text',
            'category',
            'image',
            'tags'
        )
