# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200510_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Category'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Color'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Size'),
        ),
    ]
