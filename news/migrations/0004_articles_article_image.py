# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/'),
        ),
    ]
