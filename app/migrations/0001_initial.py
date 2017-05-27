# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 18:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='FormasDePago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credito', models.BooleanField(default=False)),
                ('dedito', models.BooleanField(default=False)),
                ('efectivo', models.BooleanField(default=False)),
                ('JUNAEB', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=60)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
            options={
                'ordering': ['vendedor', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('formas_de_pago', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.FormasDePago')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='VendedorAmbulante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendedor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='VendedorFijo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_apertura', models.IntegerField()),
                ('hora_clausura', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=60)),
                ('vendedor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Vendedor')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='vendedor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Vendedor'),
        ),
        migrations.AddField(
            model_name='favorito',
            name='vendedor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Vendedor'),
        ),
    ]