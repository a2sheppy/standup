# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 23:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0017_fix_replies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='reply_to',
        ),
    ]
