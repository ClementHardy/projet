from django.shortcuts import render
from datetime import datetime
from .forms import Rdv

def home(request):
    return render(request, 'medecin/accueil.html',locals())

def dehaine(request):
    return render(request, 'medecin/dehaine.html',locals())

def dragdrop(request):
    return render(request, 'medecin/dragdrop.html', locals())

def formulaire_rdv(request):
    form = Rdv(request.POST or None)
    if form.is_valid(): 
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']
        envoi = True

    return render(request, 'medecin/formulaire.html', locals())

