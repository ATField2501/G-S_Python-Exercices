#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 55

"""
     6.3. Écrivez un programme qui calcule la période d'un pendule simple de longueur donnée.
     La formule qui permet de calculer la période d'un pendule simple est T =2 Vl/g.
     l représentant la longueur du pendule et g la valeur de l'accélération de la pesanteur au lieu
     d'expérience.

"""

from math import *

print "Calcule de la pèriode d'un pendule simple de longueur donnée ..."
long= input("longueur du pendule : ")

g = 9.81

periode= (2*pi)*sqrt(long/g)

print " La pèriode pour un pendule dont la longueur est {} et subissant l'acceleration gravitationnel en un point situer à 45°(FRANCE) est de :{}".format(long,periode)
