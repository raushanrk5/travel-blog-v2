# Generated by Django 3.1.5 on 2021-01-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210120_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(default=1, max_length=100),
        ),
    ]
