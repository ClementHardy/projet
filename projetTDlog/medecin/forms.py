# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:11:59 2016

@author: Asus
"""

from django import forms

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
)
class Rdv(forms.Form):
    nom = forms.CharField(max_length=100)
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
        if choix_1 and choix_2 and choix_3: 
            if choix_1==choix_2 or choix_1==choix_3 or choix_2==choix_3:
                 raise forms.ValidationError(
                    "veuillez classer les créneaux !"
                )
        return cleaned_data
    

class EnregistrementForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    email = forms.EmailField(label='email',widget=forms.EmailInput) 
    
    
    
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)