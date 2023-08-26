from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def index(request):
    """Главная страница"""
    posts = Post.objects.all()
    fresh = Post.objects.order_by("-date").all()[:3]
    context = {
        'posts': posts,
        'fresh': fresh

    }

    return render(request, 'publications/index.html', context=context)


def details(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    # print(post)
    context ={
        'post': post
    }

    return render(request, 'publications/details.html', context=context)
