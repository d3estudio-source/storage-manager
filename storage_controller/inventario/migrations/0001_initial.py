# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('quantidade', models.IntegerField()),
                ('item', models.CharField(max_length=255)),
                ('marca', models.CharField(blank=True, max_length=100, null=True)),
                ('modelo', models.CharField(blank=True, max_length=100, null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('caixa', models.CharField(max_length=100)),
            ],
        ),
    ]
