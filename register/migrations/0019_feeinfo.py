# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-17 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0018_auto_20160316_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='feeinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
                ('even', models.IntegerField()),
                ('odd', models.IntegerField()),
            ],
        ),
    ]