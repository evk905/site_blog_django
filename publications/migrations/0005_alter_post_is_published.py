# Generated by Django 4.2.4 on 2023-09-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0),
        ),
    ]
