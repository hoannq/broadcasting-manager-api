# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basestations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('contract_start_date', models.DateField()),
                ('contract_end_date', models.DateField()),
                ('broadcasting_hours', models.CharField(choices=[('19', '19'), ('24', '24')], default='24', max_length=2)),
                ('frequency_channel', models.CharField(blank=True, max_length=2, null=True)),
                ('power', models.CharField(blank=True, max_length=6, null=True)),
                ('broadcasting_type', models.CharField(choices=[('Vệ tinh', 'Vệ tinh'), ('Số', 'Số'), ('Tương tự', 'Tương tự')], default='Tương tự', max_length=15)),
                ('time_segment', models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
                ('machine_brand', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_by_contract', models.BooleanField(default=True)),
                ('is_by_region', models.BooleanField(default=False)),
                ('base_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basestations.Basestation')),
            ],
            options={
                'db_table': 'broadcasts',
            },
        ),
    ]
