from django.db import models
from pulp import *
import numpy as np

Nb_creneaux = 13


class Patient(models.Model):
    nom = models.CharField(max_length=100)
    motif = models.CharField(max_length=500)
    jour = models.IntegerField()
    medecin = models.IntegerField()
    choix_1 = models.IntegerField()
    choix_2 = models.IntegerField()
    choix_3 = models.IntegerField()
    affectation =models.BooleanField(default=False)
    creneau = models.IntegerField(null=True)

def Timetable(medecin,jour):
    res=[]
    n=Patient.objects.filter(medecin=medecin,jour=jour).count()
    assert(n<=Nb_creneaux)
    
    pref= [[100 for i in range(n)] for j in range(Nb_creneaux)] #pref est la matrice des préférences des patients : pref[k][i] contient le rang assigné par le patient i au créneau k
    t=[(i,j) for i in range(n) for j in range(Nb_creneaux)]
    creneaux = [i for i in range(Nb_creneaux)]
    compt=0
    lien = []
    for patient in Patient.objects.filter(medecin=medecin,jour=jour):   
        if patient.affectation == False :
            patient.affectation = True
            patient.save()
            pref[int(patient.choix_1)-1][compt]=1
            pref[int(patient.choix_2)-1][compt]=2
            pref[int(patient.choix_3)-1][compt]=3
        else :
            #il s'agit ici de s'assurer que l'affectation d'un patient ne peu plus bouger
            #à chaque fois que l'administrateur établi sont emploi du temps, les affectations
            #sont fixées
            pref[patient.creneau-1][compt] = -100
        lien.append(patient)
        compt+=1
            
    x= LpVariable.dicts('créneaux',creneaux,0, 1,LpInteger)
    y=LpVariable.dicts('assign',t,0,1,LpBinary)
    prob = LpProblem("Prise de rendez-vous",pulp.LpMinimize)
    prob += lpSum([pref[j][i]*y[(i,j)] for (i,j) in t])
    for i in range(n):
        prob+=lpSum(y[(i,j)] for j in range(Nb_creneaux))==1    
    for j in range(Nb_creneaux):
        prob+=lpSum(y[(i,j)] for i in range(n))==x[j]    
    prob.solve()
    temp=[0]*n
    for i in range(n):
        temp[i]=int(sum([(j+1)*y[(i,j)].value() for j in range(Nb_creneaux)]))
        res.append([temp[i],lien[i].nom])       
        lien[i].creneau=temp[i]
        lien[i].save()
    return res
   
    