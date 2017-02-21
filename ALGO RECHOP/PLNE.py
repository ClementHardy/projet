from pulp import *
import numpy as np
import random as rd
## Paramètres 

n=3 #nombre de patients
p=3 #nombre de créneaux
pref= [[2,1,2],[1,2,3],[3,3,1]] #pref est la matrice des préférences des patients : pref[k][i] contient le rang assigné par le patient i au créneau k

    
## Programme linéaire

#problème d'indices dans le plne suivant

t=[(i,j) for i in range(n) for j in range(p)]
creneaux = [i for i in range(p)]

x= LpVariable.dicts('créneaux',creneaux,0, 1,LpInteger)
y=LpVariable.dicts('assign',t,0,1,LpBinary)

prob = LpProblem("Prise de rendez-vous",pulp.LpMinimize)

prob += lpSum([pref[j][i]*y[(i,j)] for (i,j) in t])

for i in range(n):
    prob+=lpSum(y[(i,j)] for j in range(p))==1

for j in range(p):
    prob+=lpSum(y[(i,j)] for i in range(n))==x[j]

prob.solve()








