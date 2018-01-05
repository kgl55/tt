# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(u"欢迎光临 tt!")

def home(request):
    return render(request, 'home.html')
