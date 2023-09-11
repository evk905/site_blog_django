from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from django.db.models import Q
from .forms import PostForm
from django.contrib.auth.decorators import login_required


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
        # print(search_query)
        tags = Tag.objects.filter(name__in=hash_tags)
        posts = Post.objects.all().filter(Q(name__icontains=search_query) | Q(tags__in=tags)).distinct()
    else:
        posts = Post.objects.all().order_by("-date")

    # print(posts.query)

    fresh = Post.objects.order_by("-date").all()[:3]
    context = {
        'posts': posts,
        'fresh': fresh,
        'original_query': original_query,

    }

    return render(request, 'publications/index.html', context=context)


@login_required
def post_new(request):
    tags = Tag.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            request_tags = request.POST.getlist('tags')
            post_tags = Tag.objects.filter(name__in=request_tags)
            existing_tags = [tag.name for tag in post_tags]
            print(existing_tags)
            tags_for_create = [tag for tag in request_tags if tag not in existing_tags]
            print(tags_for_create)
            if len(tags_for_create):
                new_tags = Tag.objects.bulk_create([
                    Tag(name=name) for name in tags_for_create
                ])
                post.tags.add(*[tag for tag in new_tags])
            post.tags.add(*[tag for tag in post_tags])
            return redirect('details', post_id=post.pk)
    else:
        form = PostForm()

    context = {
        'form': form,
        'tags': tags,
    }

    return render(request, 'publications/post_edit.html', context=context)


def details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # print(post)
    context = {
        'post': post
    }

    return render(request, 'publications/details.html', context=context)


def articles(request):
    posts = Post.objects.all().order_by("-date")
    print(posts)
    context = {
        'posts': posts
    }
    return render(request, 'publications/articles.html', context=context)
