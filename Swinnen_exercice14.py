#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 55

"""
     6.4. Écrivez un programme qui permette d'encoder des valeurs dans une liste. Ce programme
     devrait fonctionner en boucle, l'utilisateur étant invité à entrer sans cesse de nouvelles
     valeurs, jusqu'à ce qu'il décide de terminer en frappant <enter> en guise d'entrée. Le
     programme se terminerait alors par l'affichage de la liste.

"""

liste_utilisateur=[]

while 1:
    objet= raw_input("Veuillez entrer une valeur: ")
    if objet != '':
        liste_utilisateur.append(objet)
    else:
        break


print liste_utilisateur
