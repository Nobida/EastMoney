# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Monetary(models.Model):

    fcode = models.AutoField(max_length=16, primary_key=True, unique=True)
    name = models.CharField(max_length=32, default='')
    value = models.CharField(max_length=32, default='')
    annualized_rate_7 = models.CharField(max_length=32, default='')
    annualized_rate_14 = models.CharField(max_length=32, default='')
    annualized_rate_28 = models.CharField(max_length=32, default='')
    starting_amount = models.IntegerField()
    score = models.IntegerField()
    record_time = models.DateTimeField(auto_now=True)
