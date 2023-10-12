from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publication/<slug:post_slug>/', views.details, name='details'),
    path('publications/articles', views.articles, name='articles'),
    path('post/new/', views.post_new, name='post_new'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),

]