# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-21 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ootlist', '0006_auto_20170921_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outoftreemodule',
            name='author',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='outoftreemodule',
            name='copyright_owner',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='outoftreemodule',
            name='icon',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='outoftreemodule',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='outoftreemodule',
            name='repo',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='outoftreemodule',
            name='tags',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='outoftreemodule',
            name='website',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
