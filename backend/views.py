from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django import forms
from .forms import UserForm
from backend import models
from .models import User


# Create your views here.
def home(request):
    return render(request, 'index.html')


def detail(request):
    return render(request, 'detail.html')


def tab(request):
    return render(request, 'tab.html')


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/index/")
