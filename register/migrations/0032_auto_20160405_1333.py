# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-05 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0031_auto_20160405_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedetail',
            name='year_sem',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='hostel_fee_detail',
            name='hostel',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
