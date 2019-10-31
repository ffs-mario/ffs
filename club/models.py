from django.db import models

from liga.models import Division

# Create your models here.
class Club(models.Model):
	"""docstring for Club"""
	nombre = models.CharField(max_length=80, blank=False, null=False)
	ciudad = models.CharField(max_length=255, blank=True, null=True)
	fundacion = models.CharField(max_length=80, blank=True, null=True)
	foto = models.ImageField(upload_to='federacion/clubes/', default='federacion/clubes/default.png')

	color1 = models.CharField(max_length=255, blank=True, null=True)
	color2 = models.CharField(max_length=255, blank=True, null=True)

	division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)


	def __str__(self):
		return self.nombre

class Fechas(models.Model):
	"""docstring for Fechas"""
	numero = models.PositiveIntegerField(default=0)
	temporada = models.PositiveIntegerField(default=0)

	equipo1 = models.PositiveIntegerField(default=0)
	equipo2 = models.PositiveIntegerField(default=0)

	division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
	jugado = models.BooleanField(default=False)

	goleslocal = models.PositiveIntegerField(blank=True, null=True)
	golesvisita = models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		return str(self.numero)

class Resultados(models.Model):
	"""docstring for Resultados"""
	local = models.PositiveIntegerField(default=0)
	visitante = models.PositiveIntegerField(default=0)
	fecha = models.ForeignKey(Fechas, on_delete=models.CASCADE, null=True)
	division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
		