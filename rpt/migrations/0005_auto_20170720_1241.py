# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpt', '0004_auto_20170630_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jirafilter',
            name='jql',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='JQL jira query'),
        ),
    ]
