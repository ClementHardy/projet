from django.test import TestCase
from pulp import *
import random
from .models import Nb_creneaux
from .models import plne

    
    

class plne_test(TestCase):
    def test_1(self):
        n = random.randint(0,Nb_creneaux-1)
        index = []
        for i in range(Nb_creneaux):
            index.append(i)
        random.shuffle(index)
        creneaux = [i for i in range(Nb_creneaux)]
        pref= [[1 for i in range(n)] for j in range(Nb_creneaux)] 
        for k in range(n):
            pref[index[k]][k] = 0
        t=[(i,j) for i in range(n) for j in range(Nb_creneaux)]
        sol = plne(creneaux,t,pref,n)
        for i in range(n):
            for j in range(Nb_creneaux):
                if pref[j][i] == 1:
                    self.assertEqual(0 == sol[(i,j)].value(),True)
                else:
                    self.assertEqual(1 == sol[(i,j)].value(),True)
                
                
