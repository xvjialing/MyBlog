# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("hello world!")
    return render(request, 'blog2/index.html')