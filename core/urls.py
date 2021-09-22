"""core URL Configuration

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
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from .views import home, redirect_somewhere
from blog.views import post_model_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^redirect/$', redirect_somewhere, name='redirect'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    #url(r'^posts/', post_model_list_view)
]
