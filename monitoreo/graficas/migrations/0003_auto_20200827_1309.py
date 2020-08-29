# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-27 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graficas', '0002_grafanadashboards_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grafanadata',
            name='uuid_organizacion',
        ),
        migrations.AlterField(
            model_name='grafanadata',
            name='token_admin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='grafanadata',
            name='token_viewer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
