# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170527_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.IntegerField(blank=True, choices=[(1, 'normal'), (2, 'vegetariano'), (3, 'vegano')], null=True),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='activo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'fijo'), (2, 'ambulante')], default=2),
        ),
    ]