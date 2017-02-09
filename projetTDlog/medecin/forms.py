# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:11:59 2016

@author: Asus
"""

from django import forms

from django.db import models
from .models import Nb_creneaux
from .models import Patient
MEDECIN = (('1','hardy'),
           ('2','dehaine'),
           ('3','janetta'),
           ('4','decottignies'),
)
JOUR = (('1','lundi'),
           ('2','mardi'),
           ('3','mercredi'),
           ('4','jeudi'),
           ('5','vendredi'),
)
CHOIX_RDV = (
    ('1', '8h'),
    ('2', '9h'),
    ('3', '10h'),
    ('4', '11h'),
    ('5', '12h'),
    ('6', '14h'),
    ('7', '14h30'),
    ('8', '15h'),
    ('9', '15h30'),
    ('10', '16h'),
    ('11', '16h30'),
    ('12', '17h'),
    ('13', '18h'),
)
class Rdv(forms.Form):
    medecin = forms.MultipleChoiceField(
        required=True,
        widget=forms.SelectMultiple,
        choices=MEDECIN,
    )
    motif = forms.CharField(widget=forms.Textarea)
    jour = forms.MultipleChoiceField(
        required=True,
        widget=forms.SelectMultiple,
        choices = JOUR,
    )
    
    choix_1 = forms.MultipleChoiceField(
        required=True,
        widget=forms.SelectMultiple,
        choices=CHOIX_RDV,
    )
    choix_2 = forms.MultipleChoiceField(
        required=True,
        widget=forms.SelectMultiple,
        choices=CHOIX_RDV,
    )
    choix_3 = forms.MultipleChoiceField(
        required=True,
       widget=forms.SelectMultiple,
       choices=CHOIX_RDV,
    )
    # la méthode suivante permet de vérifier que les créneaux sont bien ordonnés
    def clean(self):
        cleaned_data = super(Rdv, self).clean()
        choix_1 = cleaned_data.get('choix_1')
        choix_2 = cleaned_data.get('choix_2')
        choix_3 = cleaned_data.get('choix_3')
        medecin=int(cleaned_data.get('medecin')[0])
        jour=int(cleaned_data.get('jour')[0])
        if choix_1 and choix_2 and choix_3 and jour and medecin: 
            if choix_1==choix_2 or choix_1==choix_3 or choix_2==choix_3:
                 raise forms.ValidationError(
                    "veuillez classer les créneaux !"
                )
            for patient in Patient.objects.filter(medecin=medecin,jour=jour,affectation=True):
                if int(choix_1[0])==patient.creneau or int(choix_2[0])==patient.creneau or int(choix_3[0])==patient.creneau:
                    raise forms.ValidationError(
                    "Un de ces créneaux a déjà été affecté!"
                )
         
            if Patient.objects.filter(medecin=medecin,jour=jour).count() >= Nb_creneaux:
                raise forms.ValidationError(
                    "Plus de créneaux disponibles ce jour là !"
                )
        
        return cleaned_data
    

class EnregistrementForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    email = forms.EmailField(label='email',widget=forms.EmailInput) 
    
    
    
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)