from django.shortcuts import render, redirect
from liga.models import Division
from jugadores.models import Jugador
from club.models import Club, Fechas, Resultados

from random import randint

# Create your views here.

def aggdata():

	for i in range(3):
		if Division.objects.count() < 3:
			nombre = str ('Division ' + str(i+1))
			division = Division(nombre=nombre)
			division.save()
			for j in range(20):
				equipo = 'Equipo ' + str(j+1)
				club = Club(nombre=equipo, ciudad='Ciudad ' + equipo, fundacion='Fundacion ' + equipo, division=division)
				club.save()
				for k in range(10):
					njugador = 'Jugador ' + str(k+1)
					ajugador = 'Apellido ' + str(k+1)
					jugador = Jugador(nombre=njugador, apellido=ajugador, club=club)
					jugador.save()




	template = 'aggdata.html'
	return render(request,template, {})

def aggfecha(division_n):
	if Division.objects.count() < 3:
		aggdata()

	division = Division.objects.get(pk=division_n)
	club = Club.objects.filter(division_id=division_n)
	
	rango_m = club.first()
	rango_m = rango_m.id

	equipos = 20

	numero_filas = equipos - 1
	numero_columnas = int(equipos/2)

	matriz = [None] * numero_filas
	matriz2 = [None] * numero_filas
	jornada = []
	jornada_v = []

	for i in range(numero_filas):
	    matriz[i] = [None] * numero_columnas
	    matriz2[i] = [None] * numero_columnas

	count = 1
	count2 = equipos - 1
	for i in range(numero_filas):
		for j in range(numero_columnas):
			juego = []
			juego_v = []
			matriz[i][j] = count
			count = count+1;
			if count == equipos:
				count = 1;


			if j == 0:
				matriz2[i][j] = equipos
			else:
				matriz2[i][j] = count2
				count2 = count2 - 1
				if count2 == 0 :
					count2 = equipos - 1


			#jornadasida
			if j == 0:
				if i%2 == 0:
					juego.append(matriz2[i][j])
					juego.append(matriz[i][j])
					jornada.append(juego)
				else:
					juego.append(matriz[i][j])
					juego.append(matriz2[i][j])
					jornada.append(juego)
			else: 
				juego.append(matriz[i][j])
				juego.append(matriz2[i][j])
				jornada.append(juego)
			#jornadavuelta
			if j == 0:
				if i%2 == 0:
					juego_v.append(matriz[i][j])
					juego_v.append(matriz2[i][j])
					jornada_v.append(juego_v)
				else:
					juego_v.append(matriz2[i][j])
					juego_v.append(matriz[i][j])
					jornada_v.append(juego_v)
			else: 
				juego_v.append(matriz2[i][j])
				juego_v.append(matriz[i][j])
				jornada_v.append(juego_v)


	fecha = []
	fechas = []
	C = 0
	for j in range(int(equipos)-1):
		for i in range(0,int(equipos/2)):
			fecha.append(jornada[i+C])

		C = C+int(equipos/2)
		
		fechas.append(fecha)
		fecha = []

	C = 0
	for j in range(int(equipos)-1):
		for i in range(0,int(equipos/2)):
			fecha.append(jornada_v[i+C])

		C = C+int(equipos/2)
		
		fechas.append(fecha)
		fecha = []

	T = 1
	J = 1

	for x in fechas:
		for i in x:
			equipo1 = i[0]
			equipo2 = i[1]

			F = Fechas(numero=J, temporada=T, equipo1=club[equipo1-1].id, equipo2=club[equipo2-1].id, division=division)
			F.save()


		J = J+1










def inicio(request, division):
	#if Division.objects.count() < 3:
	#	aggdata()
	template = 'liga/inicio.html'

	divisionc = Division.objects.get(pk=division)
	club = Club.objects.filter(division=division)

	fecha = 0
	
	if Fechas.objects.filter(division_id=division).count() == 0:
		aggfecha(division)
	else:
		fecha = 0
	
	divisiones = Division.objects.all()

	context = {
		'club':club,
		'division':divisionc,
		'divisiones':divisiones,
	}

	return render(request, template, context)

def redireccion(request):
	return redirect('inicio', division=1)