# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Forms
from comedores.forms import comedoresForm
from comedores.forms import cuidadoresForm

from comedores.models import comedores


def infocomedores(request):
    return render(request, 'comedores/infocomedores.html')


def formcomedores(request):
    """mostrar Formulario / registrar Comedores"""
    if request.method == 'POST':
        form = comedoresForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('infocomedores')
    else:
        form = comedoresForm()
        print("else view")
    return render(request, 'comedores/formcomedores.html', {'form': form})


def infocuidadores(request):
    return render(request, 'cuidadores/infocuidadores.html')


def formcuidadores(request):
    """mostrar Formulario / registrar cuidadores"""
    if request.method == 'POST':
        form = cuidadoresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('infocuidadores')
    else:
        form = cuidadoresForm()
        print("else view")
    return render(request, 'cuidadores/formcuidadores.html', {'form': form})


def infovoluntarios(request):
    return render(request, 'infovoluntarios.html')


# def formvoluntarios(request):
#     """mostrar Formulario / registrar voluntarios"""
#     if request.method == 'POST':
#         form = voluntariosForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data)
#             return redirect('infovoluntarios')
#     else:
#         form = voluntariosForm()
#         print("else view")
#     return render(request, 'formvoluntarios.html', {'form': form})
