# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20180223_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='cover',
            field=models.CharField(default='..', max_length=50, verbose_name='头像'),
        ),
    ]