# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-26 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moving', '0007_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
