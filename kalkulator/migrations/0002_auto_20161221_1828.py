# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Racun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=20)),
                ('stanje', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Uporabnik',
        ),
    ]