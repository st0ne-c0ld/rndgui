# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpt', '0002_auto_20170620_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='jirafilter',
            name='interval',
            field=models.IntegerField(blank=True, null=True, verbose_name='Interval'),
        ),
    ]
