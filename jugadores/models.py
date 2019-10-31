from django.db import models
from club.models import Club

# Create your models here.

class Jugador(models.Model):
	"""docstring for Jugador"""
	dni = models.CharField(max_length=80, blank=True, null=True)
	nombre = models.CharField(max_length=80, blank=False, null=False)
	apellido = models.CharField(max_length=80, blank=False, null=False)
	direccion = models.CharField(max_length=255, blank=True, null=True)
	foto = models.ImageField(upload_to='federacion/jugadores/', default='federacion/jugadores/default.png')


	club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
	
	def __str__(self):
		return self.nombre + ' ' + self.apellido
