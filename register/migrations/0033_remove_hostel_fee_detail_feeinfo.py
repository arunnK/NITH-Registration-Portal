# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-05 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0032_auto_20160405_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostel_fee_detail',
            name='feeinfo',
        ),
    ]