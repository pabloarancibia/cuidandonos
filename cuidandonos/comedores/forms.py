""" comedores form """

# Django
from django import forms
from django.utils.translation import gettext_lazy as _
# Captcha
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

# Models
from comedores.models import comedores, beneficiarios, colaboradores, cuidadores, voluntarios
# from comedores.models import vountarios


# class comedoresForm(forms.Form):
# nombreCM = forms.CharField(max_length=60, required=False)
class comedoresForm(forms.ModelForm):
    """Form definition for comedores."""

    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        """Form settings."""
        model = comedores
        fields = ('__all__')
        labels = {
            'nombreCM': _('Nombre Comedor/Merendero '),
            'nombreRes': _('Nombre del responsable '),
            'apellidoRes': _('Apellido del responsable '),
            'dniRes': _('Dni del responsable '),
            'cuilRes': _('Cuil del responsable '),
            'contactoRes': _('Contacto del responsable '),
            'emailRes': _('Email del responsable '),
            'personeria': _('Nombre de Personería Juridica '),
            'cuitPersoneria': _('Cuit de Personeria Jurídica'),
            'calleCM': _('Calle del comedor/merendero '),
            'numeroCM': _('Numero de calle del comedor/merendero'),
            'manzanaCM': _('manzana del comedor/merendero'),
            'barrioCM': _('Barrio del comedor/merendero'),
            'tipoRemuneracionDS': _('Tipo de remuneración de Desarrollo Social'),
            'montoRemuneracionDS': _('Monto de remuneración de Desarrollo Social'),
            'tipoDeporte': _('Tipo de deporte que realizan'),

            'latitud': _('Marcador '),
            'longitud': _('Marcador '),
            'dias': _('Días y horarios en los que se brinda el servicio'),


        }
        error_messages = {
            'latitud': {
                'required': _("Debe agregar un marcador en el mapa, haciendo click en la ubicación deseada."),
            },
            'longitud': {
                'required': _("Debe agregar un marcador en el mapa, haciendo click en la ubicación deseada."),
            },


        }


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
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        """Form settings."""
        model = cuidadores
        fields = ('__all__')
        labels = {
            'lugarNac': _('Lugar de Nacimiento '),
            'fechaNac': _('Fecha de Nacimiento '),
            # 'nomOrg': _('Nombre Organización, asociación o fundación '),
            # 'lugarTrab': _('Lugar donde trabaja '),
            'nombreInst': _('Nombre institución'),
            'direcInst': _('Dirección institución'),
            'contactoInst': _('Contacto institución'),
            'contactoDom': _('Contacto domicilio'),
            'nombreClinica': _('Nombre clinica'),
            'direcClinica': _('Dirección clinica'),
            'contactoClinica': _('Contacto clinica'),
            'contactoFamiliar': _('Contacto familiar'),
            'nombreCoop': _('Nombre cooperativa'),

        }


class voluntariosForm(forms.ModelForm):
    """Form definition for vountarios."""

    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        """Form settings."""

        model = voluntarios
        fields = ('__all__')
        labels = {
            'lugarNac': _('Lugar de Nacimiento '),
            'fechaNac': _('Fecha de Nacimiento '),
            'nomOrg': _('Nombre Organización, asociación o fundación '),
            'lugarTrab': _('Lugar donde trabaja '),

        }
        # help_texts = {
        #     'nombre': _('Debe ingresar un nombre.'),
        # }
        # error_messages = {
        #     'nombre': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }
