# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-01 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170630_0349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgofpost',
            name='Post',
        ),
        migrations.AddField(
            model_name='imgofpost',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.Post'),
        ),
    ]
