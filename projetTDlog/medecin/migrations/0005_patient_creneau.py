# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-09 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medecin', '0004_auto_20170208_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='creneau',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]