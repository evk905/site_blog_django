from django.db import models
from authentication.models import User
from django.db.models import UniqueConstraint


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True, verbose_name='Url категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега')
    slug = models.SlugField(unique=True, verbose_name='Url тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class TagsToPosts(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег')
    post = models.ForeignKey('publications.Post', on_delete=models.CASCADE, verbose_name='Публикация')

    class Meta:
        constraints=[
            UniqueConstraint(fields=('tag', 'post'), name='unique_post_tag')
        ]


class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название публикации')
    text = models.TextField(verbose_name='Текст публикации')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(null=True, blank=True, verbose_name='Фото')
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        through=TagsToPosts,
    )



    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.name
