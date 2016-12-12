from django.shortcuts import render
from datetime import datetime


def home(request):
    return render(request, 'medecin/accueil.html',locals())

def dehaine(request):
    return render(request, 'medecin/dehaine.html',locals())