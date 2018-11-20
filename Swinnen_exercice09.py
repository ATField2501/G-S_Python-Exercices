#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 52

"""
    5.14. Écrivez un programme qui analyse un par un tous les éléments d'une liste de nombres (par
    exemple celle de l'exercice précédent) pour générer deux nouvelles listes. L'une contiendra
    seulement les nombres pairs de la liste initiale, et l'autre les nombres impairs. Par exemple,
    si la liste initiale est celle de l'exercice précédent, le programme devra construire une liste
    pairs qui contiendra [32, 12, 8, 2] , et une liste impairs qui contiendra [5, 3, 75,
    15] . Astuce : pensez à utiliser l'opérateur modulo (%) déjà cité précédemment.

"""

import sys

nb = 0
listeAAA=[]

while nb <10:
    nnn =input("Veuillez saisir un chiffres : ")
    listeAAA.append(nnn)
    nb += 1

paire=[]
impaire=[]

for index, e in enumerate(listeAAA):
    if e %2 == 1:
        impaire.append(e)
    else:
        paire.append(e)

print " Voici la liste originale : {}".format(listeAAA)
print " Celle-ci est divisée en deux listes pour séparer les nombres impaires de ceux qui sont paires"
print "nombre impaire : {}".format(impaire)
print " nombre paire : {}".format(paire)
