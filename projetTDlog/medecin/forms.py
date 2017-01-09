# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:11:59 2016

@author: Asus
"""

from django import forms



CHOIX_RDV = (
    ('1', '8h'),
    ('2', '9h'),
    ('3', '10h'),
)
class Rdv(forms.Form):
    nom = forms.CharField(max_length=100)
    motif = forms.CharField(widget=forms.Textarea)
    
    choix_1 = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CHOIX_RDV,
    )
    choix_2 = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CHOIX_RDV,
    )
    envoyeur = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

class EnregistrementForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    email = forms.EmailField(label='email',widget=forms.EmailInput) 
    
    
    
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)