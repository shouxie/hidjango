# -*- coding:utf-8 -*-
#@Time : 2020/6/18 下午5:45
#@Author: 手写
#@File : views.py
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html', {"msg": "hello"})
    # return HttpResponse('hello world!')