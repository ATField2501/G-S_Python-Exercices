#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 52

"""
    5.15. Écrivez un programme qui analyse un par un tous les éléments d'une liste de mots (par
    exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra'] pour générer deux
    nouvelles listes. L'une contiendra les mots comportant moins de 6 caractères, l'autre les
    mots comportant 6 caractères ou davantage.

"""

liste=['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra', 'Annabelle', 'Aldo', 'JustinienTrouvé', 'MK-Ultra', 'Alphonse','Albert', 'CharlesFort']
liste_moins=[]
liste_plus=[]
neo=''

for index, e in enumerate(liste):
    neo = e
    long = len(neo)
    if long >= 6:
        liste_plus.append(neo)
    else:
        liste_moins.append(neo)

print " Voici la liste comportant moins de six charactères : {}".format(liste_moins)
print " Et voici la liste comportant plus de six charactères : {}".format(liste_plus)
