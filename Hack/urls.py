"""Hack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path , include , re_path
from blog import views
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    #path(r'^user/', include('blog.urls')),

    path('newAccount/' ,include('blog.urls')),
    path('newBack/' ,include('blog.urls')),

    path('log/' ,include('blog.urls')),
    path('logBack/' ,include('blog.urls')),

    url('profile/<slug:slug>/', include('blog.urls')),
    path('ask/', include('blog.urls')),
    path('answer/', include('blog.urls')),
    path('logoutBack/', include('blog.urls')),

  #  path('' ,include('blog/urls.py')),
#    path('new1/' ,include('blog.urls')),

]
