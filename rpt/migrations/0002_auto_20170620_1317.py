# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jirafilter',
            old_name='jira_filter_id',
            new_name='jira_filter',
        ),
    ]
