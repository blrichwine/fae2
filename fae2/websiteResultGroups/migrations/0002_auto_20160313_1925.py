# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-14 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteResultGroups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteguidelineresultgroup',
            name='implementation_pass_fail_status',
            field=models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status'),
        ),
        migrations.AlterField(
            model_name='websiteguidelineresultgroup',
            name='implementation_status',
            field=models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status'),
        ),
        migrations.AlterField(
            model_name='websitereportgroup',
            name='implementation_pass_fail_status',
            field=models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status'),
        ),
        migrations.AlterField(
            model_name='websitereportgroup',
            name='implementation_status',
            field=models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status'),
        ),
        migrations.AlterField(
            model_name='websiterulecategoryresultgroup',
            name='implementation_pass_fail_status',
            field=models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status'),
        ),
        migrations.AlterField(
            model_name='websiterulecategoryresultgroup',
            name='implementation_status',
            field=models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status'),
        ),
        migrations.AlterField(
            model_name='websiteruleresultgroup',
            name='implementation_pass_fail_status',
            field=models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status'),
        ),
        migrations.AlterField(
            model_name='websiteruleresultgroup',
            name='implementation_status',
            field=models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status'),
        ),
        migrations.AlterField(
            model_name='websiterulescoperesultgroup',
            name='implementation_pass_fail_status',
            field=models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status'),
        ),
        migrations.AlterField(
            model_name='websiterulescoperesultgroup',
            name='implementation_status',
            field=models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status'),
        ),
    ]
