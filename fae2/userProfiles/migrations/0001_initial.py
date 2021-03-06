# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-07 17:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_expires', models.DateTimeField(blank=True, null=True)),
                ('org', models.CharField(blank=True, max_length=128)),
                ('dept', models.CharField(blank=True, max_length=128)),
                ('email_announcements', models.BooleanField(default=True)),
                ('timezone', timezone_field.fields.TimeZoneField(default=b'America/Chicago')),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to='accounts.AccountType')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
