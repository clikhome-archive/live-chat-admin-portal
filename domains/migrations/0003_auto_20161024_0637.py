# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-24 00:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0002_auto_20161024_0514'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Site',
            new_name='Website',
        ),
    ]
