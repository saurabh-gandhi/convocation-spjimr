# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name =models.CharField(max_length=30)
    programme =models.CharField(max_length=10)
    allowed_entries = models.IntegerField()
    remaining_entries = models.IntegerField()
