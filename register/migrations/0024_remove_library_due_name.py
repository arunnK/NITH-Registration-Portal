# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-22 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0023_library_due'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library_due',
            name='name',
        ),
    ]