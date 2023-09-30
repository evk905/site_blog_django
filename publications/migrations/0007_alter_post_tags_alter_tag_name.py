# Generated by Django 4.2.4 on 2023-09-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_alter_category_name_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='publications.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Название тега'),
        ),
    ]
