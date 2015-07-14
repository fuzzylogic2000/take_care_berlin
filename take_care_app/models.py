# -*- coding: utf-8 -*-
from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User


class KiTa(models.Model):
    # author = models.ForeignKey(User)
    # title  = models.CharField(max_length=200)
    # text   = models.TextField()

    # primary key wird automatisch erzeugt (wenn ich keinen gebe)
    kita_name    = models.CharField(max_length=256)
    traeger      = models.CharField(max_length=256, default=None, blank=True, null=True)

    adresse      = models.CharField(max_length=256)
    plz_stadt    = models.CharField(max_length=256)
    bezirk       = models.CharField(max_length=256) # to do: choices ode ManyToMany???

    lat          = models.FloatField() #Breitengrad
    lon          = models.FloatField() #Längengrad

    telefon      = models.CharField(max_length=32, default=None, blank=True, null=True)
    email        = models.EmailField(max_length=256, default=None, blank=True, null=True)
    link         = models.URLField(default=None, blank=True, null=True, help_text="Link auf Homepage der KiTa")

    beschreibung = models.TextField(default=None, blank=True, null=True, help_text="Pädagogische Schwerpunkte oder Ansätze")

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.kita_name
