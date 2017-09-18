# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('machinelocations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unitprice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broadcasting_hours', models.CharField(choices=[('19', '19'), ('24', '24')], default='24', max_length=2)),
                ('renew', models.SmallIntegerField(choices=[(1, 'Thứ nhất'), (0, 'Thứ hai')], default=0)),
                ('power_type', models.CharField(choices=[('10', '10'), ('5', '5'), ('2', '2')], default='5', max_length=2)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('machine_location', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='machinelocations.Machinelocation')),
            ],
            options={
                'db_table': 'unit_prices',
            },
        ),
    ]
