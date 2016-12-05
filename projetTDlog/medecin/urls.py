# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:39:37 2016

@author: Asus
"""

from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^accueil$', views.home),

]