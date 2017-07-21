# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . import models
# Create your views here.

from django.http import HttpResponse

def index(request):
    # return HttpResponse("hello world!")
    artical=models.Artical.objects.get(pk=1)
    return render(request, 'blog/index.html',{'artical':artical})