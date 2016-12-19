# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:11:59 2016

@author: Asus
"""

from django import forms

class Rdv(forms.Form):
    nom = forms.CharField(max_length=100)
    motif = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)