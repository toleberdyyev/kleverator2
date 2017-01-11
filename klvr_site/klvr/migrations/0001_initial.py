# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 13:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_auto_20170106_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.DateField(null=True)),
                ('price', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_author', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='auth.Tag')),
                ('workers', models.ManyToManyField(blank=True, related_name='task_workers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
