# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klvr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='tagger',
            field=models.CharField(default='null', max_length=1000),
        ),
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, to='auth.Tag'),
        ),
    ]
