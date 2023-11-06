from django import forms
from .models import Post, Tag, Category


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана",
                                      label="Категория")
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label="Теги")


    class Meta:
        model = Post
        fields = (
            'name',
            'slug',
            'text',
            'category',
            'image',
            'is_published',
            'tags',

        )
