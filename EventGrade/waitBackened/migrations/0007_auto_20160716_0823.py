# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitBackened', '0006_auto_20160716_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
