# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-27 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20160113_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitereport',
            name='last_first_page',
            field=models.IntegerField(default=0, verbose_name=b'First Page Number'),
        ),
        migrations.AlterField(
            model_name='websitereport',
            name='last_last_page',
            field=models.IntegerField(default=0, verbose_name=b'Last Page Number'),
        ),
    ]