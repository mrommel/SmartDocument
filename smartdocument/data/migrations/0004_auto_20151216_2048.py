# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20151216_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[(b'O', b'Order'), (b'B', b'Bill'), (b'T', b'Transfer')], default=b'O', max_length=1),
        ),
        migrations.AlterField(
            model_name='document',
            name='uuid',
            field=models.CharField(blank=True, default='cc078e1b-2093-4abc-b364-492913894a7a', editable=False, max_length=36),
        ),
    ]
