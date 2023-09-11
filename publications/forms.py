from django import forms
from .models import Post, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'name',
            'text',
            'category',
            'image',
            # 'tags',
        )

# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = (
#             'name',
#         )
#         # fields = '__all__' если все поля нужны

