# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-05 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_id', models.IntegerField(default=0)),
                ('title', models.CharField(default=b'no account type title', max_length=64)),
                ('description', models.TextField(blank=True, default=b'')),
                ('description_html', models.TextField(blank=True, default=b'')),
                ('max_archive', models.IntegerField(default=10)),
                ('max_permanent', models.IntegerField(default=5)),
                ('max_depth', models.IntegerField(default=2)),
                ('max_pages', models.IntegerField(default=25)),
                ('advanced', models.BooleanField(default=False)),
                ('protected', models.BooleanField(default=False)),
                ('default', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['type_id'],
                'verbose_name': 'Account Type',
                'verbose_name_plural': 'Account Types',
            },
        ),
    ]
