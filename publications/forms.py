from django import forms
from .models import Post, Tag, Category


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана",
                                      label="Категории")


    class Meta:
        model = Post
        fields = (
            'name',
            'slug',
            'text',
            'category',
            'image',

        )
