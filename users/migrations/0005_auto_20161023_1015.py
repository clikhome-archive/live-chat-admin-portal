# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-23 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20161022_0455'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='chatuser',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='userban',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='chatuser',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chatuser',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='chatuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='chatuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
        ),
        migrations.AlterField(
            model_name='chatuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterUniqueTogether(
            name='chatuser',
            unique_together=set([('username', 'channel'), ('phone', 'channel')]),
        ),
    ]
