# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-09 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_auto_20190707_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='worked_till',
            field=models.DateField(blank=True, null=True),
        ),
    ]