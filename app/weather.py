import requests
from datetime import datetime
from .secret_key import KEY

def getWeather(city):
    # Sukuriama URL su miesto pavadinimu, API raktais, matavimo vienetais ir kalba
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric&lang=lt'

    # Siunčiama GET užklausa į URL ir gaunamas atsakymas kaip JSON
    response = requests.get(url).json()

    # Gaunamas dabartinis laikas
    current_time = datetime.now()

    # Dabartinis laikas formatuojamas į žmogui suprantamą formatą
    formatted_time = current_time.strftime('%A, %B %d %Y, %H:%M:%S %p')

    # Sukuriamas kontekstas su orų duomenimis iš API atsakymo
    context = {
        'city': city,
        'description': response['weather'][0]['description'], # Orų aprašymas
        'icon': response['weather'][0]['icon'], # Orų ikona
        'temperature': 'Temperatūra: ' +  str(response['main']['temp']), # Temperatūra
        'country_code': response['sys']['country'], # Šalies kodas
        'wind': 'Vėjas: ' + str(response['wind']['speed']) + 'km/h', # Vėjo greitis
        'humidity': 'Drėgmė: ' + str(response['main']['humidity']) + '%', # Drėgmė
        'time': formatted_time # Suformatuotas dabartinis laikas
    }

    # Grąžinamas kontekstas su orų informacija
    return context