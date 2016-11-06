# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-21 22:55
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20161009_1048'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='chatuser',
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='userban',
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='chatuser',
            name='ip',
        ),
    ]
