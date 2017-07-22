# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

import json

from . import models
# Create your views here.

def index(request):
    # return HttpResponse("hello world!")
    #artical=models.Artical.objects.get(pk=1) #获取主键为1的值
    articals=models.Artical.objects.all() #获取全部的值
    return render(request, 'blog/index.html',{'articals':articals})

def article_page(request,article_id):
    article=models.Artical.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id)=='0':
        return render(request,'blog/edit_page.html')
    article = models.Artical.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})

def edit_action(request):
    title=request.POST.get('title','Title')
    content=request.POST.get('content','Content')
    article_id=request.POST.get('article_id','0')
    if article_id=='0':
        models.Artical.objects.create(title=title,content=content)
        articals = models.Artical.objects.all()  # 获取全部的值
        return render(request, 'blog/index.html', {'articals': articals})
    else:
        article=models.Artical.objects.get(pk=article_id)
        article.title=title
        article.content=content
        article.save()
        return render(request, 'blog/article_page.html', {'article': article})

def toDicts(objs):
    obj_arr=[]
    for o in objs:
        obj_arr.append(o.toDict())
    return obj_arr

def getArticles(request):
    # articals = models.Artical.objects.get(pk=1) # 获取全部的值
    # articals_dicts=toDicts(articals)
    # return HttpResponse(json.dump(articals_dicts),ensure_ascii=False,content_type='application/json')

    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
