# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-07 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatuser',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
