# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import EgreForm, AdminForm
from .models import Egresado

from random import choice

# Create your views here.

def index(request):
	return render(request, "index.html", {})

def registrarEg(request):
	egform = EgreForm(request.POST or None)
	context = {
		"formEg" : egform,
	}

	if egform.is_valid():
		valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
		contra = ""
		form_data = egform.cleaned_data
		idegresado = form_data.get("idegresado")
		pnombre = form_data.get("pnombre")
		snombre = form_data.get("snombre")
		papellido = form_data.get("papellido")
		sapellido = form_data.get("sapellido")
		pais = form_data.get("pais") 
		correo = form_data.get("correo")
		contra = contra.join([choice(valores) for i in range(8)])
		genero = form_data.get("genero")
		carrera = form_data.get("carrera")
		grado = form_data.get("grado")
		estado = 0
		obj = Egresado.objects.create(idegresado=idegresado, pnombre=pnombre, snombre=snombre, 
			papellido=papellido, sapellido=sapellido, pais=pais, correo=correo, contra=contra, 
			genero=genero, carrera=carrera, grado=grado, estado=estado)

		send_mail(
			'Registro Plataforma Egresados UTP',
	   		"Genial! Registro Completado\nBienvenido {} {}\nTu contraseña de ingreso es {}".format(pnombre, papellido, contra),
	 		settings.EMAIL_HOST_USER,
    		[correo],
    		fail_silently=False,
		)

		context = {
			"InfoCorreo" : "Te enviaremos un correo a {} con tu contraseña de ingreso cuando seas activado".format(correo),
			"InfoGracias" : "Gracias {} {}, UTP Egresados ☺".format(pnombre, papellido),
		}

	return render(request, "regEgresado.html", context)

def registrarAdmin(request):
	return render(request, "regAdmin.html", {})