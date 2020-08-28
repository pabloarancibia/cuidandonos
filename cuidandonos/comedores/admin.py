from django.contrib import admin
from comedores.models import voluntarios


@admin.register(voluntarios)
class voluntariosAdmin(admin.ModelAdmin):
    """voluntarios Admin"""
    pass
