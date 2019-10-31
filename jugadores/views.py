from django.shortcuts import render

from .models import Jugador
from club.models import Club

# Create your views here.

def jugador(request, club, jugador):
	template = 'jugador/jugador.html'

	J = Jugador.objects.get(pk=jugador)
	equipo = Club.objects.get(pk=club)
	context = {
		'jugador':J,
		'club':equipo,
	}
	return render(request, template, context)