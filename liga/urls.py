from django.urls import path
from .views import aggdata, inicio, redireccion

urlpatterns = [
    path('aggdata/', aggdata, name='aggdata'),
    path('<int:division>', inicio, name='inicio'),
    path('', redireccion, name='redireccion')
]
