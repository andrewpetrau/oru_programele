from django.urls import path # Importuojamas 'path' iš Django URL bibliotekos
from .views import index # Importuojamas 'index' vaizdas iš views.py failo

urlpatterns = [
    path('', index, name='home'), # Nustatoma maršruto taisyklė
    # Ši eilutė nurodo, kad jei vartotojas eina į pagrindinį puslapį (tuščias kelias ''),
    # bus paleistas 'index' vaizdas, o 'home' yra vardas, kurį galite naudoti kituose koduose,
    # kad kreiptumėtės į šį maršrutą (pvz., naudojant Django 'reverse' funkciją)
]
