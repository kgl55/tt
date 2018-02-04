"""tt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from backend import views as backend_views
from calc import views as calc_views

urlpatterns = {
    path('', backend_views.home, name='home'),
    re_path('^index/', backend_views.home, name='index'),
    re_path('^tab/', backend_views.tab, name='tab'),
    path('admin/', admin.site.urls),
    re_path('^detail/', backend_views.detail, name='detail'),
    re_path('^login*', backend_views.login, name='login'),
    re_path('^register*', backend_views.register, name='register'),
    re_path('^logout*', backend_views.logout, name='logout'),
    # path('add2/<int:a>/<int:b>/', calc_views.add2, name='add2'),

}
