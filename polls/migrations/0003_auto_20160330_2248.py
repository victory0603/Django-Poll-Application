# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 05:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160330_1738'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
