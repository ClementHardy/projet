from django.shortcuts import render
from datetime import datetime

# connexion utilisateur
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

#formulaires
from .forms import Rdv
from .forms import ConnexionForm

def home(request):
    return render(request, 'medecin/accueil.html',locals())

def dehaine(request):
    return render(request, 'medecin/dehaine.html',locals())

def dragdrop(request):
    return render(request, 'medecin/dragdrop.html', locals())

def formulaire_rdv(request):
    form = Rdv(request.POST or None)
    if form.is_valid(): 
        #permet de rendre le formulaire utilisable
        #pour une autre utilisation
        nom = form.cleaned_data['nom']
        motif = form.cleaned_data['motif']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']
        envoi = True
        #on rempli la base de donnée ici !!!
        

    return render(request, 'medecin/formulaire.html', locals())


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'medecin/connexion.html', locals())
    
def deconnexion(request):
    logout(request)
    return render(request, 'medecin/deconnexion.html',locals())