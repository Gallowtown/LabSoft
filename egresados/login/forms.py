from django import forms
from .models import Egresado, Administrador

class EgreForm(forms.ModelForm):
	class Meta:
		model = Egresado
		fields = ["idegresado", "pnombre", "snombre", "papellido", "sapellido", "pais", "correo", "genero", "carrera", "grado"]

	def clean_correo(self):
		email = self.cleaned_data.get("correo")
		base, exten = email.split("@")
		if not "utp.edu.co" == exten:
			raise forms.ValidationError("Ingrese por favor el correo institucional")
		return email

class AdminForm(forms.ModelForm):
	class Meta:
		model = Administrador
		fields = ["idadmon", "pnombre", "snombre", "papellido", "sapellido", "correo", "contra", "genero"]
