# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeavedInventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_id',
            field=models.AutoField(default=5, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='product_code',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
