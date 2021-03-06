# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20151216_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date_ordered', models.DateTimeField()),
                ('date_bill_received', models.DateTimeField()),
                ('date_payed', models.DateTimeField()),
                ('status', models.CharField(choices=[(b'U', b'Unsure'), (b'O', b'Ordered'), (b'N', b'Open'), (b'P', b'Payed')], default=b'U', max_length=1)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='document',
            name='uuid',
            field=models.CharField(blank=True, default='ce64774f-ae36-4d07-acf3-262ee710aba6', editable=False, max_length=36),
        ),
        migrations.AddField(
            model_name='document',
            name='entry',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='data.Entry'),
            preserve_default=False,
        ),
    ]
