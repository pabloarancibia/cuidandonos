""" comedores form """

# Django
from django import forms

# Models
from comedores.models import comedores
from comedores.models import cuidadores
# from comedores.models import vountarios


# class comedoresForm(forms.Form):
# nombreCM = forms.CharField(max_length=60, required=False)
class comedoresForm(forms.ModelForm):
    """Form definition for comedores."""

    class Meta:
        """Form settings."""

        model = comedores
        fields = ('__all__')


class cuidadoresForm(forms.ModelForm):
    """Form definition for cuidadores."""

    class Meta:
        """Form settings."""

        model = cuidadores
        fields = ('__all__')


# class vountariosForm(forms.ModelForm):
#     """Form definition for vountarios."""

#     class Meta:
#         """Form settings."""

#         model = vountarios
#         fields = ('__all__')
