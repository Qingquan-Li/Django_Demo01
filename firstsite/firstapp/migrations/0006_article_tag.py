# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'life')], max_length=5, null=True),
        ),
    ]
