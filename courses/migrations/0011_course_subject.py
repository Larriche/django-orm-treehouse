# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
