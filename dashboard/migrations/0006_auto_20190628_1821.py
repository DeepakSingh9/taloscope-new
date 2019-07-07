# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-28 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20190628_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follows',
        ),
        migrations.AddField(
            model_name='profile',
            name='followed_by',
            field=models.ManyToManyField(related_name='follows', to='dashboard.Profile'),
        ),
    ]