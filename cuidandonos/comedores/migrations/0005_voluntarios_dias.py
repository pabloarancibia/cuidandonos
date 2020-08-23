# Generated by Django 3.1 on 2020-08-22 21:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comedores', '0004_auto_20200820_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='voluntarios',
            name='dias',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
    ]
