#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 55

"""
     6.1. Écrivez un programme qui convertisse en mètres par seconde et en km/h une vitesse fournie
     par l'utilisateur en miles/heure. (Rappel : 1 mile = 1609 mètres)
"""


mimile=raw_input('Veuillez rentrer une valeurs en miles par heure que le programme convertira en km/h :')

mimile = int(mimile)
metrik=mimile*1.609344

print metrik


