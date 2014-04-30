# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Cines(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=50)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    descripcion = models.TextField()
    web = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'cines'

class Horarios(models.Model):
    id_cine = models.IntegerField()
    id_peli = models.IntegerField()
    horarios = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'horarios'

class Peliculas(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=255)
    titulo_original = models.CharField(max_length=255)
    elenco = models.TextField()
    director = models.CharField(max_length=255)
    sinopsis = models.TextField()
    thumb = models.CharField(max_length=255)
    trailer = models.CharField(max_length=255)
    fecha_alta = models.DateTimeField()
    id_rc = models.IntegerField()
    url_rc = models.CharField(max_length=255)
    origen = models.CharField(max_length=255)
    anio = models.CharField(max_length=10)
    duracion = models.CharField(max_length=20)
    genero = models.CharField(max_length=255)
    horarios_txt = models.TextField()
    estreno = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'peliculas'

