#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 55

"""
     6.2. Écrivez un programme qui calcule le périmètre et l'aire d'un triangle        quelconque dont
     l'utilisateur fournit les 3 côtés.
     (Rappel : l'aire d'un triangle quelconque se calcule à l'aide de la formule :
     S =  d⋅d −a⋅d −b⋅d −c
     dans laquelle d désigne la longueur du demi-périmètre, et a, b, c celles des trois côtés).
"""

from math import *

print "Calcule de l'aire d'un triangle ..."


cote1=input('Veuillez rentrer la valeur du premier coté : ')
cote2=input('Veuillez rentrer la valeur du deuxième coté : ')
cote3=input('Veuillez rentrer la valeur du troisième coté : ')




somme =(cote1 + cote2 + cote3)*1/2

print "le demi-périmètre est de {}".format(somme)

try:
    surface= sqrt(somme*(somme-cote1)*(somme-cote2)*(somme-cote3))
except:
    surface="--Calcul Impossible--"

print "La surface du triangle dont les cotés sont {},{},{} est :{}".format(cote1,cote2,cote3,surface)
