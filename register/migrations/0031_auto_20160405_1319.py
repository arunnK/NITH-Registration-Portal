# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-05 13:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0030_auto_20160403_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedetail',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hostel_fee_detail',
            name='feeinfo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.feeinfo'),
        ),
        migrations.AddField(
            model_name='hostel_fee_detail',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
