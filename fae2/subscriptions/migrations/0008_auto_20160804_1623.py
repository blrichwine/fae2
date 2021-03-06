# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-04 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_auto_20160726_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='actual_subscription_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='reference_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='subscription_cost',
            field=models.IntegerField(default=0),
        ),
    ]
