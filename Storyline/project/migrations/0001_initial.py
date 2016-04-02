# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('theme', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('by', models.ForeignKey(related_name='Contributor', to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='chapter_followers')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=1000)),
                ('commented_at', models.DateTimeField(auto_now_add=True)),
                ('chapter', models.ForeignKey(related_name='comment_on_chapter', to='project.chapter')),
                ('commented_by', models.ForeignKey(related_name='Commented_by', to=settings.AUTH_USER_MODEL)),
                ('liked_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='liked_by')),
            ],
        ),
        migrations.CreateModel(
            name='story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('theme', models.CharField(max_length=100)),
                ('idea', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('by', models.ForeignKey(related_name='story_creator', to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='story_followers')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='story',
            field=models.ForeignKey(related_name='comment_on_story', to='project.story'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='story',
            field=models.ForeignKey(related_name='story', to='project.story'),
        ),
    ]
