from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def infocomedores(request):
    return render(request, 'infocomedores.html')


def formcomedores(request):
    return render(request, 'formcomedores.html')
