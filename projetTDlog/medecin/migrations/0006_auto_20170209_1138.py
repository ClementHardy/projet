# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-09 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medecin', '0005_patient_creneau'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='creneau',
            field=models.IntegerField(null=True),
        ),
    ]