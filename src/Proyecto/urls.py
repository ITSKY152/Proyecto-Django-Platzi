"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from fila_de_banco.views import fila
from fila_de_banco.views import AgregarD
from PlatziClean.views import PlatziClean
from PlatziClean.views import AgregarP
from PlatziData.views import PlatziData
from PlatziData.views import AgregarL
from django.shortcuts import render

def inicio(request):
    return render(request,'inicio.html',{})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('Banco', fila),
    path('Clean', PlatziClean),
    path('Data', PlatziData),
    path('AgregarD', AgregarD),
    path('AgregarP', AgregarP),
    path('AgregarL', AgregarL),
]
