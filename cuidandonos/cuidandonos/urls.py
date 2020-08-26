"""cuidandonos URL Configuration

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
from django.shortcuts import render
from django.urls import path

from comedores import views


urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('comedores/infocomedores/',
         views.infocomedores, name='infocomedores'),
    path('comedores/formcomedores/',
         views.formcomedores, name='formcomedores'),
    path('cuidadores/infocuidadores/',
         views.infocuidadores, name='infocuidadores'),
    path('cuidadores/formcuidadores/',
         views.formcuidadores, name='formcuidadores'),
    path('voluntariado/infovoluntarios/',
         views.infovoluntarios, name='infovoluntarios'),
    path('voluntariado/formvoluntarios/',
         views.formvoluntarios, name='formvoluntarios'),
    path('informacion/contactos/',
         views.contactos, name='contactos'),

    path('mapa/', views.mapa, name='mapa'),




]
