# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Forms
from comedores.forms import comedoresForm, beneficiariosForm, colaboradoresForm
from comedores.forms import cuidadoresForm, voluntariosForm

from comedores.models import comedores, cuidadores, beneficiarios, colaboradores, voluntarios


def infocomedores(request):
    return render(request, 'comedores/infocomedores.html')


def formcomedores(request):
    """mostrar Formulario / registrar Comedores/Merenderos"""
    if request.method == 'POST':
        cmform = comedoresForm(request.POST, instance=comedores())
        cm_valid = cmform.is_valid()
        if cm_valid:
            # recorrer lista beneficiarios y colaboradores segun
            cantBenef = cmform.cleaned_data["cantBenef"]
            cantColab = cmform.cleaned_data["cantColab"]
            bnforms = [beneficiariosForm(request.POST, prefix=str(
                x), instance=beneficiarios()) for x in range(0, cantBenef)]
            clforms = [colaboradoresForm(request.POST, prefix=str(
                x), instance=colaboradores()) for x in range(0, cantColab)]

            bn_valid = all([bnf.is_valid() for bnf in bnforms])
            cl_valid = all([clf.is_valid() for clf in clforms])

            if cm_valid and bn_valid and cl_valid:
                cm = cmform.save()
                for bnf in bnforms:
                    bn = bnf.save(commit=False)
                    bn.comMerBenef = cm
                    bn.save()
                for clf in clforms:
                    cl = clf.save(commit=False)
                    cl.comMerCol = cm
                    cl.save()
            else:
                print("algun formulario no es valido")
        else:
            print("formulario CM no válido")
            bnforms = [beneficiariosForm(prefix=str(
                x), instance=beneficiarios())for x in range(0, 1)]
            clforms = [colaboradoresForm(request.POST, prefix=str(
                x), instance=colaboradores()) for x in range(0, 1)]
    else:
        cmform = comedoresForm(instance=comedores())
        bnforms = [beneficiariosForm(prefix=str(
            x), instance=beneficiarios())for x in range(0, 1)]
        clforms = [colaboradoresForm(request.POST, prefix=str(
            x), instance=colaboradores()) for x in range(0, 1)]

    return render(request,
                  'comedores/formcomedores.html',
                  {
                      'cmform': cmform, 'bnforms': bnforms, 'clforms': clforms
                  })


def infocuidadores(request):
    return render(request, 'cuidadores/infocuidadores.html')


def formcuidadores(request):
    """mostrar Formulario / registrar cuidadores"""
    if request.method == 'POST':
        form = cuidadoresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            return redirect('infocuidadores')
    else:
        form = cuidadoresForm()
        # print("else view")
    return render(request, 'cuidadores/formcuidadores.html', {'form': form})


def infovoluntarios(request):
    return render(request, 'voluntariado/infovoluntarios.html')


def formvoluntarios(request):
    """mostrar Formulario / registrar voluntarios"""
    if request.method == 'POST':
        form = voluntariosForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            return redirect('infovoluntarios')
    else:
        form = voluntariosForm()
        # print("else view")
    return render(request, 'voluntariado/formvoluntarios.html', {'form': form})
