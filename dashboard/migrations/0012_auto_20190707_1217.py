# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-07 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20190707_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profilepic/astro2.jpg', null=True, upload_to='profilepic/'),
        ),
    ]