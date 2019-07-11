# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contact(models.Model):
    sender=models.EmailField()
    name=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.sender


