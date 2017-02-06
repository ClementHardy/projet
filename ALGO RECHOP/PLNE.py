from pulp import *
import numpy as np

## Paramètres 

n=3 #nombre de patients
p=3 #nombre de créneaux
pref= [[1,2,3],[2,1,3],[3,2,1]] #pref est la matrice des préférences des patients : pref[k][i] contient le rang assigné par le patient i au créneau k

    
## Programme linéaire


t=[(i,j) for i in range(n) for j in range(p)]

x= LpVariable.dicts('créneaux', creneaux,0, 1,LpInteger)
y=LpVariable.dicts('assign',t,0,1,LpBinary)

prob = LpProblem("Prise de rendez-vous",pulp.LpMinimize)

prob += lpSum([pref[i][j]*y[(i,j)] for (i,j) in t])

for i in range(n):
    prob+=lpSum(y[(i,j)] for j in range(p))==1

for j in range(n):
    prob+=lpSum(y[(i,j)] for i in range(n))==x[j]

prob.solve()

res=[0]*n
for i in range(n):
    res[i]=int(sum([j*y[(i,j)].value() for j in range(p)]))
    print("Le patient {} est assigné au créneau {}".format(i+1,res[i]+1))


    






