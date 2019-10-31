from django.urls import path
from .views import club

urlpatterns = [
    path('<int:id>', club, name='club'),

]

