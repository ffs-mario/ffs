from django.urls import path
from .views import jugador

urlpatterns = [
	path('club/<int:club>/jugador/<int:jugador>', jugador, name='jugador'),
]
