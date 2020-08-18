""" comedores form """

# Django
from django import forms

# Models
from comedores.models import comedores, beneficiarios, colaboradores, cuidadores, voluntarios
# from comedores.models import vountarios


# class comedoresForm(forms.Form):
# nombreCM = forms.CharField(max_length=60, required=False)
class comedoresForm(forms.ModelForm):
    """Form definition for comedores."""
    class Meta:
        """Form settings."""
        model = comedores
        fields = ('__all__')


class beneficiariosForm(forms.ModelForm):
    """seccion beneficiarios form"""
    class Meta:
        model = beneficiarios
        exclude = ('comMerBenef',)


class colaboradoresForm(forms.ModelForm):
    """seccion colaboradores form"""
    class Meta:
        model = colaboradores
        exclude = ('comMerCol',)


class cuidadoresForm(forms.ModelForm):
    """Form definition for cuidadores."""
    class Meta:
        """Form settings."""
        model = cuidadores
        fields = ('__all__')


class voluntariosForm(forms.ModelForm):
    """Form definition for vountarios."""

    class Meta:
        """Form settings."""

        model = voluntarios
        fields = ('__all__')
