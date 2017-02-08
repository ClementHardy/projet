# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('motif', models.CharField(max_length=500)),
                ('jour', models.CharField(max_length=10)),
                ('medecin', models.CharField(max_length=20)),
                ('choix_1', models.CharField(max_length=30)),
                ('choix_2', models.CharField(max_length=30)),
                ('choix_3', models.CharField(max_length=30)),
            ],
        ),
    ]