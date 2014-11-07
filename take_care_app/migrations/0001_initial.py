# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KiTa',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('kita_name', models.CharField(max_length=256)),
                ('traeger', models.CharField(max_length=256)),
                ('adresse', models.CharField(max_length=256)),
                ('plz_stadt', models.CharField(max_length=256)),
                ('bezirk', models.CharField(max_length=256)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('telefon', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=256)),
                ('link', models.URLField(help_text='Link auf Homepage der KiTa', blank=True)),
                ('beschreibung', models.TextField(help_text='Pädagogische Schwerpunkte oder Ansätze')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
