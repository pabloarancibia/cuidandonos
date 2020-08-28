from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    """ Perfil Model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cuil = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    # def__str__(self):
    #     """Return username."""
    #     return self.user.username
