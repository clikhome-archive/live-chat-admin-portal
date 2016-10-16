# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-03 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=uuid.uuid4, max_length=50, verbose_name='Unique token')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('is_used', models.BooleanField(default=False)),
                ('started_at', models.DateTimeField(blank=True, null=True, verbose_name='Started at')),
                ('expiry_at', models.DateTimeField(blank=True, null=True, verbose_name='Expiry at')),
                ('stopped_at', models.DateTimeField(blank=True, null=True, verbose_name='Stoped at')),
                ('channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='channel_token', to='channels.Channel')),
            ],
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TokenDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('days', models.IntegerField(default=0, verbose_name='Days')),
                ('months', models.IntegerField(default=0, verbose_name='Months')),
                ('years', models.IntegerField(default=0, verbose_name='Years')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='duration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='token_duration', to='tokens.TokenDuration'),
        ),
    ]
