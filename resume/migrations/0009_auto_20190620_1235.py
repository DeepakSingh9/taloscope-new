# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-20 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='designation',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='organisation',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='worked_till',
            field=models.DateField(blank=True),
        ),
    ]
