from django.shortcuts import render, get_object_or_404
from .models import Post, Tag
from django.db.models import Q


# Create your views here.
def index(request):
    """Главная страница"""

    search_query = request.GET.get('search')
    original_query = search_query

    if search_query:
        words = search_query.split()
        hash_tags = []
        for word in words:
            if word[0] == "#":
                search_query = search_query.replace(word, "")
                hash_tags.append(word[1:])
        search_query = search_query.strip()
        print(search_query)
        tags = Tag.objects.filter(name__in=hash_tags)
        posts = Post.objects.all().filter(Q(name__icontains=search_query)|Q(tags__in=tags)).distinct()
    else:
        posts = Post.objects.all().order_by("-date")

    print(posts.query)

    fresh = Post.objects.order_by("-date").all()[:3]
    context = {
        'posts': posts,
        'fresh': fresh,
        'original_query': original_query,

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
