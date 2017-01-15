# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:39:37 2016

@author: Asus
"""

from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^accueil$', views.home),
    url(r'^dehaine$', views.dehaine),
    url(r'^decottignies$', views.decottignies),
    url(r'^jannetta$', views.jannetta),
    url(r'^hardy$', views.hardy),
    url(r'^dragdrop$', views.dragdrop),
    url(r'^formulaire/$', views.formulaire_rdv, name='formulaire'),
    url(r'^connexion$', views.connexion, name='connexion'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
    url(r'^enregistrement$', views.enregistrement, name='enregistrement'),
    

]