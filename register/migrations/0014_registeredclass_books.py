# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-13 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20160312_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredclass',
            name='books',
            field=models.IntegerField(default=0),
        ),
    ]
