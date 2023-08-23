from django.shortcuts import render
from .weather import getWeather # Importuojama funkcija getWeather iš weather.py failo

# Sukuriamas vaizdas index
def index(request):
    try: # Bandome vykdyti kodą ir pagauti bet kokias klaidas
        if request.method == 'POST': # Tikriname, ar užklausa yra POST tipo
            city = request.POST['city'] # Gauname miesto pavadinimą iš POST duomenų
            context = getWeather(city) # Gauname orų informaciją naudodamiesi getWeather funkcija
            return render(request, 'home.html', context) # Atvaizduojame home.html šabloną su orų kontekstu
        else: # Jei užklausa nėra POST tipo
            city_weather = {} # Sukuriamas tuščias žodynas orų informacijai
            context = {'city_weather': city_weather} # Kontekstas su tuščiu orų žodynų
            return render(request, 'home.html', context) # Atvaizduojame home.html šabloną su tuščiu orų kontekstu
    except: # Jei įvyko klaida (pvz., blogai suformatuoti duomenys, problema su API)
        return render(request, 'error.html') # Atvaizduojame klaidos puslapį error.html
