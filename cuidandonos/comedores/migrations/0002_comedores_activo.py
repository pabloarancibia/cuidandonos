# Generated by Django 3.1 on 2020-08-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comedores',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]