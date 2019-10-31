from django.db import models

# Create your models here.

class Division(models.Model):
	"""docstring for Division"""
	nombre = models.CharField(max_length=80, blank=False, null=False)
	logo = models.ImageField(upload_to='federacion/liga/', default='federacion/liga/default.png')
	
	def __str__(self):
		return self.nombre

