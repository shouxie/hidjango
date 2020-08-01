# -*- coding:utf-8 -*-
#@Time : 2020/6/18 下午7:21
#@Author: 手写
#@File : urls.py
from django.urls import path

from userapp.views import getUser
urlpatterns = [
    path('list', getUser)
]
