# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Egresado(models.Model):
	idegresado = models.CharField(primary_key = True, max_length = 25)
	pnombre = models.CharField(max_length = 25)
	snombre = models.CharField(max_length = 25)
	papellido = models.CharField(max_length = 25)
	sapellido = models.CharField(max_length = 25)
	pais = models.CharField(max_length = 25)
	correo = models.EmailField(max_length = 50)
	contra = models.CharField(max_length = 25) 
	genero = models.CharField(max_length = 25)
	carrera = models.CharField(max_length = 50)
	grado = models.DateField()
	estado = models.IntegerField()

	def __unicode__(self):
		return unicode(self.idegresado) 

class Administrador(models.Model):
	idadmon = models.IntegerField(primary_key = True)
	pnombre = models.CharField(max_length = 25)
	snombre = models.CharField(max_length = 25)
	papellido = models.CharField(max_length = 25)
	sapellido = models.CharField(max_length = 25)
	correo = models.EmailField(max_length = 25)
	contra = models.CharField(max_length = 25) 
	genero = models.CharField(max_length = 25)
	estado = models.IntegerField()

	def __unicode__(self):
		return unicode(self.idadmon)