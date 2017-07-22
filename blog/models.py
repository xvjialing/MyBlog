# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Artical(models.Model):
    title=models.CharField(max_length=32,default='title')
    content=models.TextField(null=True)
    pub_time = models.DateField(null=True)

    def __unicode__(self):
        return self.title
