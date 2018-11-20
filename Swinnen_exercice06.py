#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 52

"""
    5.11. Soient les listes suivantes :
          t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
          t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
          'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
          Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les
          éléments des deux listes en les alternant, de telle manière que chaque nom de mois soit
          suivi du nombre de jours correspondant : ['Janvier',31,'Février',28,'Mars',31,etc...] .


"""

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

neo_liste=[]
long = len(t2)
nb=0

while nb < long:
    neo_liste.append(t2[nb])
    neo_liste.append(t1[nb])
    nb +=1
            
    
print neo_liste

