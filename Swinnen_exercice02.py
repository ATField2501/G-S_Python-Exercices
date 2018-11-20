#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 49
# 5.7 Ecrivez un script qui compte le nombre d'occurrences du caractère « e » dans une chaîne.
	
import sys

cible= 'e'
nb=0

for arg in sys.argv: 
    chaine = arg

for e in chaine:
    if cible in e:
        nb +=1
print "La chaine comporte exactement : {} {}".format(nb, cible)
