# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150601_1513'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Step',
            new_name='Text',
        ),
    ]
