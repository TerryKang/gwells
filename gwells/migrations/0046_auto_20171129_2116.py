# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-29 21:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0045_auto_20171128_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='LithologyDescriptionCode',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30, null=True)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('lithology_description_code_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_lithology_description_code',
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterModelOptions(
            name='lithologydescription',
            options={},
        ),
        migrations.AddField(
            model_name='lithologydescription',
            name='lithology_description',
            field=models.ForeignKey(blank=True, db_column='lithology_description_code_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.LithologyDescriptionCode', verbose_name='Description'),
        ),
    ]