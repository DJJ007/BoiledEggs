# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 02:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20170629_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.RemoveField(
            model_name='author',
            name='publications',
        ),
    ]