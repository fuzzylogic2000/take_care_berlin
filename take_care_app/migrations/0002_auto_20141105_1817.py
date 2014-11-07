# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('take_care_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kita',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='kita',
            name='beschreibung',
        ),
        migrations.RemoveField(
            model_name='kita',
            name='bezirk',
        ),
        migrations.RemoveField(
            model_name='kita',
            name='email',
        ),
        migrations.RemoveField(
            model_name='kita',
            name='link',
        ),
        migrations.RemoveField(
            model_name='kita',
            name='plz_stadt',
        ),
        migrations.RemoveField(
            model_name='kita',
            name='telefon',
        ),
        migrations.RemoveField(
            model_name='kita',
            name='traeger',
        ),
    ]
