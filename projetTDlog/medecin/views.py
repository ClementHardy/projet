from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# connexion utilisateur
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

#formulaires
from .forms import Rdv
from .forms import ConnexionForm,EnregistrementForm
from .forms import CHOIX_RDV
#modèles
from .models import Patient
from .models import Timetable
from .models import Nb_creneaux
from .models import JOUR
def home(request):
    return render(request, 'medecin/accueil.html',locals())

def calendrier(request):
    return render(request, 'medecin/calendrier.html',locals())

def profil(request):
    res=[]
    for patient in Patient.objects.filter(nom=User.username, affectation = True):
        res.append([patient.creneau,JOUR[patient.jour-1][1]])
    return render(request, 'medecin/profil.html',locals())


def execution(request,medecin,jour):
    res = Timetable(medecin,jour)
    for i in range(len(res)):
        res[i][0]=CHOIX_RDV[res[i][0]-1][1]

    return render(request, 'medecin/execution.html',locals())
    

    

def formulaire_rdv(request):
    form = Rdv(request.POST or None)
    envoi = False
    if form.is_valid(): 

        data = form.clean()
        patient = Patient.objects.create(nom=User.username,motif = data.get('motif'),jour=int(data.get('jour')[0]), medecin=int(data.get('medecin')[0]),choix_1=int(data.get("choix_1")[0]),choix_2=int(data.get("choix_2")[0]),choix_3=int(data.get("choix_3")[0]))        
        envoi = True
        
        

    return render(request, 'medecin/formulaire.html', locals())


def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password) # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'medecin/connexion.html', locals())
    
    
    
def enregistrement(request):
    form = EnregistrementForm(request.POST)
    enregistre = False
    if form.is_valid():
        enregistre = True
        user = User.objects.create_user(form.cleaned_data["username"],form.cleaned_data["email"],form.cleaned_data['password'])
       
    return render(request, 'medecin/enregistrement.html', locals())
    
    
def deconnexion(request):
    logout(request)
    return render(request, 'medecin/deconnexion.html',locals())