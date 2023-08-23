"""
URL configuration for weather project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Importuojamas Django administracijos modulis
from django.urls import path, include # Importuojami 'path' ir 'include' iš Django URL bibliotekos

urlpatterns = [
    path('admin/', admin.site.urls), # Nustatoma maršruto taisyklė administracijos svetainei
    # Ši eilutė nurodo, kad visi URL, prasidedantys 'admin/', bus nukreipti į Django administracijos svetainę

    path('', include('app.urls')), # Nustatoma maršruto taisyklė, kuri įtraukia kitą URL konfigūraciją
    # Ši eilutė nurodo, kad visi kiti URL maršrutai bus perduoti į 'app.urls' konfigūraciją.
    # Tai reiškia, kad visos taisyklės, aprašytos 'app.urls' faile, bus taikomos šiam projektui.
    # Tai leidžia organizuoti URL konfigūraciją moduliai, kiekvienas susijęs su atskira aplikacija projekte.
]

