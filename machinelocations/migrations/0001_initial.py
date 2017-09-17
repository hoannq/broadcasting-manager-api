# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machinelocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Địa điểm đặt máy cùng với Đài địa phương', 'Địa điểm đặt máy cùng với Đài địa phương'), ('Địa điểm đặt máy đặc biệt khó khăn', 'Địa điểm đặt máy đặc biệt khó khăn'), ('Cụm máy phát độc lập của Đài Truyền hình Quốc gia', 'Cụm máy phát độc lập của Đài Truyền hình Quốc gia'), ('Địa điểm đặt máy bình thường', 'Địa điểm đặt máy bình thường'), ('Địa điểm đặt máy đặc biệt khó khăn', 'Địa điểm đặt máy đặc biệt khó khăn')], max_length=100)),
                ('owner', models.CharField(choices=[('Đài Truyền hình Quốc gia', 'Đài Truyền hình Quốc gia'), ('Đài Truyền hình Địa phương', 'Đài Truyền hình Địa phương')], max_length=100)),
            ],
        ),
    ]