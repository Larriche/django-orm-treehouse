# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-03 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_course_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='times_taken',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
