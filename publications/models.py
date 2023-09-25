from django.db import models
from django.urls import reverse

from authentication.models import User

from .utils import slugify


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
    name = models.CharField(max_length=255, verbose_name='Название тега', unique=True)
    slug = models.SlugField(unique=True, verbose_name='Url тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    # def save(
    #     self, *args, **kwargs
    # ):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название публикации')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    text = models.TextField(verbose_name='Текст публикации')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(null=True, blank=True, verbose_name='Фото')
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
    )
    is_published = models.BooleanField(default=True)



    class Meta:
        ordering = ['-date'] #порядок сортировки
        indexes = [models.Index(fields=['-date'])] #сделать поля индексируемыми
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'post_slug': self.slug})
