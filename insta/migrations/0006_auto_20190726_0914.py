# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-26 06:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20190724_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profilepic',
            new_name='profilepicture',
        ),
    ]