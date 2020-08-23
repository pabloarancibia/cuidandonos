from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import file_size

# Create your models here.


class comedores (models.Model):
    """Comedores Model"""
    srvComedor = models.BooleanField(default=False)
    srvMerendero = models.BooleanField(default=False)
    nombreCM = models.CharField(
        max_length=60, help_text="Debe ingresar un nombre para el comedor/merendero")

    nombreRes = models.CharField(max_length=60)
    apellidoRes = models.CharField(max_length=60)
    dniRes = models.BigIntegerField()
    cuilRes = models.BigIntegerField(max_length=11)
    contactoRes = models.BigIntegerField()
    emailRes = models.EmailField()

    perteneceOrg = models.CharField(max_length=2, default='no')
    personeria = models.CharField(max_length=60, blank=True, null=True)
    cuitPersoneria = models.BigIntegerField(blank=True, null=True)

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

    dias = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(2), MaxValueValidator(7)])

    cantColab = models.IntegerField()

    remuneracionDS = models.CharField(max_length=2, default='no')
    tipoRemuneracionDS = models.CharField(max_length=60, blank=True, null=True)
    montoRemuneracionDS = models.IntegerField(blank=True, null=True)

    aguaCM = models.CharField(max_length=2, default='no')
    tipoConex = models.CharField(max_length=10, default='externa')
    instElec = models.CharField(max_length=2, default='no')
    espacioCerradoCM = models.CharField(max_length=2, default='no')
    sanitarioCM = models.CharField(max_length=2, default='no')
    banoCM = models.BooleanField(default=False)
    letrinaCM = models.BooleanField(default=False)
    otrosCM = models.BooleanField(default=False)
    cocinaCM = models.CharField(max_length=2, default='no')

    huerta = models.CharField(max_length=2, default='no')
    deporte = models.CharField(max_length=2, default='no')
    tipoDeporte = models.CharField(max_length=60, blank=True, null=True)
    apoyoEsc = models.CharField(max_length=2, default='no')
    infoHigiene = models.CharField(max_length=2, default='no')
    educSex = models.CharField(max_length=2, default='no')
    prevViolencia = models.CharField(max_length=2, default='no')
    prevConsumo = models.CharField(max_length=2, default='no')


class beneficiarios (models.Model):
    """ Beneficiarios de Comedores/Merenderos Model"""
    inputNombreBenef = models.CharField(max_length=100)
    inputDniBenef = models.BigIntegerField()
    comMerBenef = models.ForeignKey(
        comedores, on_delete=models.SET_NULL, null=True)


class colaboradores (models.Model):
    """ Colaboradores de Com/Mer Model"""
    nomCol = models.CharField(max_length=80)
    apCol = models.CharField(max_length=80)
    dniCol = models.BigIntegerField()
    cuilCol = models.BigIntegerField()
    comMerCol = models.ForeignKey(
        comedores, on_delete=models.SET_NULL, null=True)


class cuidadores (models.Model):
    """ cuidadores Model"""

    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    dni = models.BigIntegerField()
    cuil = models.BigIntegerField()
    lugarNac = models.CharField(max_length=80)
    fechaNac = models.DateField()
    genero = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    barrio = models.CharField(max_length=80)
    localidad = models.CharField(max_length=80)
    provincia = models.CharField(max_length=80)
    celular = models.BigIntegerField()
    email = models.EmailField()
    rdEstudioMax = models.CharField(max_length=80)
    titulo = models.CharField(max_length=80)
    institucion = models.CharField(max_length=80)
    rdGeriatria = models.CharField(max_length=80)
    archivoGeriatria = models.FileField(
        upload_to='archivos/cuidadores', blank=True, null=True, validators=[file_size])
    rdCapacita = models.CharField(max_length=80)
    rdLeyDH = models.CharField(max_length=80)
    rdCapEdSex = models.CharField(max_length=80)
    rdExperiencia = models.CharField(max_length=80)
    rdLugarExperiencia = models.CharField(max_length=80, blank=True, null=True)
    nombreInst = models.CharField(max_length=80, blank=True, null=True)
    direcInst = models.CharField(max_length=80, blank=True, null=True)
    contactoInst = models.CharField(max_length=80, blank=True, null=True)
    contactoDom = models.CharField(max_length=80, blank=True, null=True)
    nombreClinica = models.CharField(max_length=80, blank=True, null=True)
    direcClinica = models.CharField(max_length=80, blank=True, null=True)
    contactoClinica = models.CharField(max_length=80, blank=True, null=True)
    contactoFamiliar = models.CharField(max_length=80, blank=True, null=True)
    rdCoopTr = models.CharField(max_length=80)
    nombreCoop = models.CharField(max_length=80, blank=True, null=True)
    archivoDniAsp = models.FileField(
        upload_to='archivos/cuidadores', validators=[file_size])
    archivoCertAsp = models.FileField(
        upload_to='archivos/cuidadores', validators=[file_size])
    archivoCertDomAsp = models.FileField(
        upload_to='archivos/cuidadores', validators=[file_size])
    arhivoCertPsfAsp = models.FileField(
        upload_to='archivos/cuidadores', validators=[file_size])
    archivoCertReinc = models.FileField(
        upload_to='archivos/cuidadores', validators=[file_size])


class voluntarios(models.Model):
    """ voluntarios model"""
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    dni = models.BigIntegerField()
    cuil = models.BigIntegerField()
    lugarNac = models.CharField(max_length=80)
    fechaNac = models.DateField()
    genero = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    barrio = models.CharField(max_length=80)
    localidad = models.CharField(max_length=80)
    provincia = models.CharField(max_length=80)
    celular = models.BigIntegerField()
    email = models.EmailField()

    rdEstudiante = models.CharField(max_length=2)
    estudios = models.CharField(max_length=80, blank=True, null=True)
    rdOrg = models.CharField(max_length=2)
    nomOrg = models.CharField(max_length=80, blank=True, null=True)
    rdTrabaja = models.CharField(max_length=2)
    lugarTrab = models.CharField(max_length=80, blank=True, null=True)
    rdProfesion = models.CharField(max_length=2)
    profestion = models.CharField(max_length=80, blank=True, null=True)

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

    comentario = models.CharField(max_length=800)
    rdLeyVol = models.CharField(max_length=2)
