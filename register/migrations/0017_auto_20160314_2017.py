# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-14 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_auto_20160314_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredclass',
            name='rollno',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
