# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-19 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0010_auto_20200917_1910'),
        ('userApp', '0002_auto_20200916_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_creattime', models.DateTimeField(auto_now_add=True)),
                ('o_totalprice', models.FloatField()),
                ('o_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.User')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='orderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('og_goods_num', models.IntegerField()),
                ('og_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Goods')),
                ('og_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderApp.Order')),
            ],
            options={
                'db_table': 'order_goods',
            },
        ),
    ]