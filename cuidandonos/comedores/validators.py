from django.core.exceptions import ValidationError


def file_size(value):
    limit = 20 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(
            'No puede subir archivos que superen los 20mb.')
    else:
        return value
