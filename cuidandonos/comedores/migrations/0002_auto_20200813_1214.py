# Generated by Django 3.1 on 2020-08-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comedores',
            name='perteneceOrg',
            field=models.CharField(default='no', max_length=2),
        ),
    ]
