from functools import reduce

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag, Category
from django.db.models import Q
from operator import or_
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from .utils import slugify


# Create your views here.
def index(request):
    """Главная страница"""
    search_query = request.GET.get('search')
    if search_query:
        words = search_query.split()
        posts = Post.published.filter(reduce(or_, [Q(name__icontains=w) for w in words])).prefetch_related('tags')
    else:
        posts = Post.published.all().prefetch_related('tags')

    fresh = Post.published.all()[:3]
    context = dict(posts=posts, fresh=fresh, search_query=search_query)

    return render(request, 'publications/index.html', context=context)


@login_required
def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # name = form.cleaned_data.get('name')
            # post.slug = slugify(name)
            post.save()
            form.save_m2m()

            return redirect('details', post_slug=post.slug)
    else:
        form = PostForm()

    context = {
        'form': form,

    }

    return render(request, 'publications/post_edit.html', context=context)


def details(request, post_slug):
    post = get_object_or_404(Post.objects.select_related('author'), slug=post_slug)
    # print(post)
    context = {
        'post': post
    }

    return render(request, 'publications/details.html', context=context)


def articles(request):
    posts = Post.published.all().prefetch_related('tags')
    # print(posts)
    context = {
        'posts': posts
    }
    return render(request, 'publications/articles.html', context=context)

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = tag.tags.filter(is_published=Post.Status.PUBLISHED)
    context = {
        'posts': posts

    }
    return render(request, 'publications/articles.html', context=context)

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Post.published.filter(category_id=category.pk)

    data = {
        'title': category.name,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'publications/index.html', context=data)