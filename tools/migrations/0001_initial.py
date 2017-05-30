# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 11:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('related_tag', models.ManyToManyField(blank=True, default=None, related_name='_tag_related_tag_+', to='tools.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('icon_url', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('video_url', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('tagline', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('description', models.TextField(blank=True, default=None, max_length=300, null=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, default=None, to='tools.Tag')),
            ],
        ),
    ]
