# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-17 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='is_select',
            field=models.BooleanField(default=True),
        ),
    ]
