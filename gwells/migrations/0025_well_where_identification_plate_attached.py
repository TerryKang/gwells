# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-14 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0024_remove_well_well_identification_plate_attached'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='where_identification_plate_attached',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Where Identification Plate Is Attached'),
        ),
    ]
