# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
