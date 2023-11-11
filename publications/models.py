from django.db import models
from django.urls import reverse

from authentication.models import User



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Post.Status.PUBLISHED)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Url категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега', unique=True, db_index=True)
    slug = models.SlugField(max_length=300, unique=True, verbose_name='Url тега', db_index=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    name = models.CharField(max_length=255, verbose_name='Название публикации')
    slug = models.SlugField(max_length=300, unique=True, db_index=True, verbose_name='Слаг')
    text = models.TextField(verbose_name='Текст публикации')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='posts', verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Автор')
    image = models.ImageField(null=True, blank=True, verbose_name='Фото')
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True, related_name='tags')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), verbose_name='Статус', default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-date']  # порядок сортировки
        indexes = [models.Index(fields=['-date'])]  # сделать поля индексируемыми
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'post_slug': self.slug})
