"""
===========================
File Name: views.py
Date: 2019/6/9
Software: PyCharm
Author: li_pin
===========================
"""

from django.shortcuts import render_to_response

def home(request):
    context ={}

    return render_to_response('home.html',context)