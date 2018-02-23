# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_users_pwd'),
        ('Log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
        migrations.AddField(
            model_name='logcomment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
        migrations.AddField(
            model_name='logreply',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
        migrations.AlterField(
            model_name='logreply',
            name='reply',
            field=models.CharField(max_length=140, verbose_name='回复'),
        ),
    ]