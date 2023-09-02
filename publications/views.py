from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def index(request):
    """Главная страница"""
    search_query = request.GET.get('search')
    if search_query:
        posts = Post.objects.all().filter(name__istartswith=search_query)
    else:
        posts = Post.objects.all().order_by("-date")

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
