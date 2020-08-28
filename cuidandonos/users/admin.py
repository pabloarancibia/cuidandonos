from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from users.models import Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    """ Perfil Admin """
    list_display = ('user', 'cuil', 'telefono')

    list_editable = ('telefono',)

    search_fields = (
        'cuil',
    )
    list_filter = ('creado', 'modificado')

    fieldsets = (
        ('Perfil', {
            'fields': (('user', 'cuil', 'telefono'),),
        }),
    )


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
