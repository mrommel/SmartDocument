# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_document_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uuid',
            field=models.CharField(blank=True, default='22519271-eb4f-4feb-9698-46f53090508d', editable=False, max_length=36),
        ),
    ]
