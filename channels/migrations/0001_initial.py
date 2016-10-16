# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-03 03:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=uuid.uuid4, max_length=50, unique=True, verbose_name='Unique id')),
                ('title', models.CharField(help_text='Only for the admin portal', max_length=50, verbose_name='Title channel')),
                ('site', models.URLField(help_text='Site that chat will use')),
                ('domain', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('superuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'channel',
                'verbose_name_plural': 'Channels',
            },
        ),
    ]