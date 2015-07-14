# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('take_care_app', '0002_auto_20141105_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='kita',
            name='adresse',
            field=models.CharField(max_length=256, default='Petersburger Str. 95'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kita',
            name='beschreibung',
            field=models.TextField(blank=True, null=True, help_text='Pädagogische Schwerpunkte oder Ansätze', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kita',
            name='bezirk',
            field=models.CharField(max_length=256, default='Friedrichshain'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kita',
            name='email',
            field=models.EmailField(blank=True, max_length=256, null=True, default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kita',
            name='link',
            field=models.URLField(blank=True, null=True, help_text='Link auf Homepage der KiTa', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kita',
            name='plz_stadt',
            field=models.CharField(max_length=256, default='10247 Berlin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kita',
            name='telefon',
            field=models.CharField(blank=True, max_length=32, null=True, default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kita',
            name='traeger',
            field=models.CharField(blank=True, max_length=256, null=True, default=None),
            preserve_default=True,
        ),
    ]
