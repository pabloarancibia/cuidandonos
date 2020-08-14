from django.db import models

# Create your models here.


class comedores (models.Model):
    """Comedores Model"""
    srvComedor = models.BooleanField(default=False)
    srvMerendero = models.BooleanField(default=False)
    nombreCM = models.CharField(max_length=60)

    nombreRes = models.CharField(max_length=60)
    apellidoRes = models.CharField(max_length=60)
    dniRes = models.IntegerField()
    cuilRes = models.IntegerField()
    contactoRes = models.IntegerField()
    emailRes = models.EmailField()

    perteneceOrg = models.CharField(max_length=2, default='no')
    personeria = models.CharField(max_length=60)
    cuitPersoneria = models.IntegerField()

    benefDS = models.CharField(max_length=2, default='no')
    tipoModulos = models.BooleanField(default=False)
    tipoKit = models.BooleanField(default=False)
    tipoPrograma = models.BooleanField(default=False)
    tipoInversion = models.BooleanField(default=False)
    tipoInsumo = models.BooleanField(default=False)

    calleCM = models.CharField(max_length=60)
    numeroCM = models.IntegerField()
    manzanaCM = models.CharField(max_length=60)
    barrioCM = models.CharField(max_length=60)
    provinciaCM = models.CharField(max_length=60)
    localidadCM = models.CharField(max_length=60)

    cantBenef = models.IntegerField()
    grupoAdultos = models.BooleanField(default=False)
    grupoMujEmb = models.BooleanField(default=False)
    grupoJov = models.BooleanField(default=False)
    grupoAdolec = models.BooleanField(default=False)
    grupoNino = models.BooleanField(default=False)
    grupoCalle = models.BooleanField(default=False)
    grupoDisc = models.BooleanField(default=False)

    # aparte clase beneficiarios ya que es una relacion 1 comedor N beneficiarios
    # en esta deberá ir idComedor nombre apellido.

    trLunes = models.BooleanField(default=False)
    hrDesdeLun = models.TimeField()
    hrHastaLun = models.TimeField()
    trMartes = models.BooleanField(default=False)
    hrDesdeMar = models.TimeField()
    hrHastaMar = models.TimeField()
    trMierdoles = models.BooleanField(default=False)
    hrDesdeMier = models.TimeField()
    hrHastaMier = models.TimeField()
    trJueves = models.BooleanField(default=False)
    hrDesdeJuev = models.TimeField()
    hrHastaJuev = models.TimeField()
    trViernes = models.BooleanField(default=False)
    hrDesdeVier = models.TimeField()
    hrHastaVier = models.TimeField()
    trSabado = models.BooleanField(default=False)
    hrDesdeSab = models.TimeField()
    hrHastaSab = models.TimeField()
    trDomingo = models.BooleanField(default=False)
    hrDesdeDom = models.TimeField()
    hrHastaDom = models.TimeField()

    # colaboradores lo mismo que beneficiarios

    remuneracionDS = models.CharField(max_length=2, default='no')
    tipoRemuneracionDS = models.CharField(max_length=60)

    aguaCM = models.CharField(max_length=2, default='no')
    tipoConex = models.CharField(max_length=10)
    instElec = models.CharField(max_length=2, default='no')
    espacioCerradoCM = models.CharField(max_length=2, default='no')
    sanitarioCM = models.CharField(max_length=2, default='no')
    banoCM = models.BooleanField(default=False)#
    letrinaCM = models.BooleanField(default=False)#
    otrosCM = models.BooleanField(default=False)#
    cocinaCM = models.CharField(max_length=2, default='no')

    huerta = models.CharField(max_length=2, default='no')
    deporte = models.CharField(max_length=2, default='no')
    tipoDeporte = models.CharField(max_length=60)
    apoyoEsc = models.CharField(max_length=2, default='no')
    infoHigiene = models.CharField(max_length=2, default='no')
    educSex = models.CharField(max_length=2, default='no')
    prevViolencia = models.CharField(max_length=2, default='no')
    prevConsumo = models.CharField(max_length=2, default='no')
