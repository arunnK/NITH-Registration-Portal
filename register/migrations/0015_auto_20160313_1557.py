# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-13 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_registeredclass_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredclass',
            name='books',
            field=models.IntegerField(default=12),
        ),
    ]
