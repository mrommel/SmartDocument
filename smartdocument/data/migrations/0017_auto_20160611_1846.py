# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-11 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_auto_20160123_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='creditable',
            field=models.CharField(choices=[(b'U', b'Unsure'), (b'Y', b'Yes'), (b'N', b'No')], default=b'U', max_length=1),
        ),
        migrations.AlterField(
            model_name='document',
            name='uuid',
            field=models.CharField(blank=True, default='7e98dbc9-ba64-46ae-b62f-00af0ab63a5e', editable=False, max_length=36),
        ),
    ]
