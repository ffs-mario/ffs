from django.shortcuts import render, get_object_or_404


from .models import Club, Fechas
from jugadores.models import Jugador



# Create your views here.

def club(request, id):
	club = get_object_or_404(Club, pk=id)
	jugadores = Jugador.objects.filter(club_id=id)


	query = Fechas.objects.filter(equipo1=id, jugado=False) | Fechas.objects.filter(equipo2=id, jugado=False)
	fecha = query.first()
	
	juegos = query[:5]

	adversario = fecha.equipo1

	if adversario == club.id:
		adversario = fecha.equipo2

	rival = Club.objects.get(pk=adversario)

	prox_juegos = []

	for x in juegos:
		if x.equipo1 == club.id:
			prox_juegos.append(x.equipo2)
		else:
			prox_juegos.append(x.equipo1)
			
	prox = []
	for x in prox_juegos:
		prox.append(Club.objects.get(pk=x))

	template = 'club/club.html'
	context = {
		'club':club,
		'jugadores':jugadores,
		'rival':rival,
		'proximos':prox,
	}
	return render(request,template,context)