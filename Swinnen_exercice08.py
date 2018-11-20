#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 52

"""
    5.13. Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée.
    Par exemple, si on l'appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15] , ce programme
    devrait afficher :
    le plus grand élément de cette liste a la valeur 75.

"""

import sys

nb = 0
listeAAA=[]

while nb <5:
    nnn =input("Veuillez saisir un chiffres : ")
    listeAAA.append(nnn)
    nb += 1

listeAAA.sort()

for index,elt in enumerate(listeAAA):
    ouranos = ''
    ouranos = elt


print "le plus grand élément de cette liste a la valeur {}.".format(ouranos)


