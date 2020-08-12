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

    perteneceOrg = models.BooleanField(default=False)
    personeria = models.CharField(max_length=60)
    cuitPersoneria = models.IntegerField()

    benefDS = models.BooleanField(default=False)
    tipoModulos = models.BooleanField(default=False)
    tipoKit = models.BooleanField(default=False)
    tipoPrograma = models.BooleanField(default=False)
    tipoInversion = models.BooleanField(default=False)
    tipoInsumo = models.BooleanField(default=False)

    calleCM = models.CharField(max_length=60)
    numeroCM = models.IntegerField()
    manzanaCM = models.IntegerField()
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

    remuneracionDS = models.BooleanField(default=False)
    tipoRemuneracionDS = models.CharField(max_length=60)

    aguaCM = models.BooleanField(default=False)
    tipoConexInt = models.BooleanField(default=False)
    tipoConexExt = models.BooleanField(default=False)
    instElec = models.BooleanField(default=False)
    espacioCM = models.BooleanField(default=False)
    sanitarioCM = models.BooleanField(default=False)
    banoCM = models.BooleanField(default=False)
    letrinaCM = models.BooleanField(default=False)
    otrosCM = models.BooleanField(default=False)
    cocinaCM = models.BooleanField(default=False)

    huerta = models.BooleanField(default=False)
    deporte = models.BooleanField(default=False)
    tipoDeporte = models.CharField(max_length=60)
    apoyoEsc = models.BooleanField(default=False)
    infoHigiene = models.BooleanField(default=False)
    educSex = models.BooleanField(default=False)
    prevViolencia = models.BooleanField(default=False)
    prevConsumo = models.BooleanField(default=False)
