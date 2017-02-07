from django.db import models
from pulp import *
import numpy as np

Nb_creneaux = 3


class Patient(models.Model):
    nom = models.CharField(max_length=100)
    motif = models.CharField(max_length=500)
    jour = models.CharField(max_length=10)
    medecin = models.CharField(max_length=20)
    choix_1 = models.CharField(max_length=30)
    choix_2 = models.CharField(max_length=30)
    choix_3 = models.CharField(max_length=30)
    affectation =models.BooleanField(default=False)

def Timetable(medecin,jour):
    res=[]
    pref= [[0 for i in range(Nb_creneaux)] for j in range(Nb_creneaux)] #pref est la matrice des préférences des patients : pref[k][i] contient le rang assigné par le patient i au créneau k
    t=[(i,j) for i in range(Nb_creneaux) for j in range(Nb_creneaux)]
    creneaux = [i for i in range(Nb_creneaux)]
    compt=0
    lien = []
    for patient in Patient.objects.filter(medecin=[str(medecin)],jour=[str(jour)]):   
        lien.append(patient.motif)
        pref[int(patient.choix_1)-1][compt]=1
        pref[int(patient.choix_2)-1][compt]=2
        pref[int(patient.choix_3)-1][compt]=3 
        compt+=1
    
    x= LpVariable.dicts('créneaux',creneaux,0, 1,LpInteger)
    y=LpVariable.dicts('assign',t,0,1,LpBinary)
    prob = LpProblem("Prise de rendez-vous",pulp.LpMinimize)
    prob += lpSum([pref[i][j]*y[(i,j)] for (i,j) in t])
    for i in range(Nb_creneaux):
        prob+=lpSum(y[(i,j)] for j in range(Nb_creneaux))==1    
    for j in range(Nb_creneaux):
        prob+=lpSum(y[(i,j)] for i in range(Nb_creneaux))==x[j]    
    prob.solve()
    temp=[0]*Nb_creneaux
    for i in range(Nb_creneaux):
        temp[i]=int(sum([j*y[(i,j)].value() for j in range(Nb_creneaux)]))
        res.append([temp[i]+1,lien[i]])
    return res
        
    