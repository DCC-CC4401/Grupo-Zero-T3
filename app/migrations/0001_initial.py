# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 15:59
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
            name='Favorito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['alumno', 'vendedor'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, default='img/bread', upload_to='media')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('categoria', models.IntegerField(choices=[(1, 'normal'), (2, 'vegetariano'), (3, 'vegano')], default=1)),
            ],
            options={
                'ordering': ['vendedor', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, default='img/avatarEstudiante3.png', upload_to='media')),
                ('tipo', models.IntegerField(choices=[(1, 'admin'), (2, 'alumno'), (3, 'vendedor')], default=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credito', models.BooleanField(default=False)),
                ('debito', models.BooleanField(default=False)),
                ('efectivo', models.BooleanField(default=False)),
                ('JUNAEB', models.BooleanField(default=False)),
                ('tipo', models.IntegerField(choices=[(1, 'fijo'), (2, 'ambulante')], default=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Usuario')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='VendedorAmbulante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=False)),
                ('vendedor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='VendedorFijo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_apertura', models.TimeField()),
                ('hora_clausura', models.TimeField()),
                ('ubicacion', models.CharField(max_length=60)),
                ('vendedor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Producto')),
            ],
            options={
                'ordering': ['fecha', 'producto'],
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Vendedor'),
        ),
        migrations.AddField(
            model_name='favorito',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Usuario'),
        ),
        migrations.AddField(
            model_name='favorito',
            name='vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Vendedor'),
        ),
    ]
