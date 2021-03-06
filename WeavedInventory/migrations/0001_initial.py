# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-11 15:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('product_code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_field', models.CharField(max_length=20)),
                ('option_value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserActionLog',
            fields=[
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_action', models.CharField(max_length=10)),
                ('log_msg', models.CharField(max_length=60)),
                ('time', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('variant_id', models.AutoField(primary_key=True, serialize=False)),
                ('cost', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('item_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WeavedInventory.Item')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='variant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WeavedInventory.Variant'),
        ),
    ]
