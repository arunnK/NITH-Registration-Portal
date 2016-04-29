# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('rollno', models.CharField(max_length=8)),
                ('mobile', models.PositiveIntegerField(max_length=10)),
                ('branch', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('pincode', models.PositiveIntegerField(max_length=6)),
            ],
        ),
    ]