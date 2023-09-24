from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publications/<int:post_id>/', views.details, name='details'),
    path('publications/articles', views.articles, name='articles'),
    path('post/new/', views.post_new, name='post_new'),

]