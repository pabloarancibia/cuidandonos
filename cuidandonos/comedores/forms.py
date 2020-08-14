""" comedores form """

# Django
from django import forms

# Models
from comedores.models import comedores

# class comedoresForm(forms.Form):
    # nombreCM = forms.CharField(max_length=60, required=False)
class comedoresForm(forms.ModelForm):
    """Form definition for comedores."""

    class Meta:
        """Form settings."""

        model = comedores
        fields = ('__all__')