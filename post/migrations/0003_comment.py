# Generated by Django 3.1.5 on 2021-01-20 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('comment_author', models.CharField(max_length=70, verbose_name='Name')),
                ('comment_content', models.CharField(max_length=200, verbose_name='Comment')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post')),
            ],
            options={
                'ordering': ('comment_date',),
            },
        ),
    ]
