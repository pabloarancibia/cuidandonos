# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Forms
from comedores.forms import comedoresForm
from comedores.models import comedores




def infocomedores(request):
    return render(request, 'infocomedores.html')


def formcomedores(request):
    """mostrar Formulario / registrar Comedores"""
    if request.method == 'POST':
            form = comedoresForm(request.POST)
            if form.is_valid():
                form.save()
                print(form.cleaned_data)
                return redirect ('comedores')
    else:
        form = comedoresForm()
        print("else view")
    return render(request,'formcomedores.html', {'form':form})