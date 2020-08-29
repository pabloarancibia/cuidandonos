from django.contrib import admin
from comedores.models import voluntarios


@admin.register(voluntarios)
class voluntariosAdmin(admin.ModelAdmin):
    """voluntarios Admin"""
    list_display = ('nombre', 'apellido', 'dni', 'cuil', 'lugar_Nac', 'fecha_Nac',
                    'genero', 'direccion', 'barrio', 'localidad', 'provincia', 'celular', 'email')

    # lugarNac.short_description = 'Lugar de Nacimiento'

    def lugar_Nac(self, obj):
        return obj.lugarNac
    lugar_Nac.short_description = 'Lugar de Nacimiento'

    def fecha_Nac(self, obj):
        return obj.fechaNac
    fecha_Nac.short_description = 'Fecha de Nacimiento'
