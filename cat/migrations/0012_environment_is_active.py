# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0011_auto_20170602_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='environment',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
        ),
    ]
