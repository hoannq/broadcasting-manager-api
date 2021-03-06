# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('televisions', '0001_initial'),
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basestation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('manage_type', models.CharField(choices=[('Hợp đồng', 'Hợp đồng'), ('Trực tiếp', 'Trực tiếp')], default=0, max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='areas.Area')),
                ('television', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='televisions.Television')),
            ],
            options={
                'db_table': 'base_stations',
            },
        ),
    ]
