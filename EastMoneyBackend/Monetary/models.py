# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Monetary(models.Model):

    primary_key = models.CharField(max_length=8, primary_key=True, unique=True,default='')
    fcode = models.CharField(max_length=8,default='')
    name = models.CharField(max_length=32, default='')
    value = models.CharField(max_length=32, default='')
    score = models.IntegerField()
    record_time = models.DateTimeField(auto_now=True)
    tendency = models.CharField(max_length=32,default='')
    starting_amount = models.CharField(max_length=8,default='')
