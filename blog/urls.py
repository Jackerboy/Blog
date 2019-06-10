"""
===========================
File Name: urls.py
Date: 2019/6/9
Software: PyCharm
Author: li_pin
===========================
"""

from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # /blog/1
    path('',views.blog_list,name = 'blog_list'),
    path('<int:blog_id>',views.bolg_datail,name = "bg_detail"),
    path('type/<type_id>',views.blog_type_list,name = "type_list"),
]