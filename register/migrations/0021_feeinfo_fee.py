# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-18 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0020_auto_20160318_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeinfo',
            name='fee',
            field=models.IntegerField(default=0),
        ),
    ]