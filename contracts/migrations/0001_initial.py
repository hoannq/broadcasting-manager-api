# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unitprices', '0001_initial'),
        ('broadcasts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.CharField(max_length=20)),
                ('sign_date', models.DateField()),
                ('contract_type', models.CharField(choices=[('Khai thác', 'Khai thác'), ('Tiếp phát', 'Tiếp phát')], default='Khai thác', max_length=10)),
                ('tax', models.DecimalField(choices=[(5.0, 5.0), (10.0, 10.0)], decimal_places=2, default=10.0, max_digits=5)),
                ('cancel_date', models.DateField(blank=True, null=True)),
                ('broadcast', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='broadcasts.Broadcast')),
                ('unit_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unitprices.Unitprice')),
            ],
            options={
                'db_table': 'contracts',
            },
        ),
    ]
