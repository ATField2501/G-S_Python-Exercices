#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 52

"""
    5.12. Écrivez un programme qui affiche « proprement » tous les éléments d'une liste. Si on
    l'appliquait par exemple à la liste t2 de l'exercice ci-dessus, on devrait obtenir :
    Janvier Février Mars Novembre Décembre

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

chaine_propre=''
            
for element in neo_liste:
    element=str(element)
    chaine_propre += element
    chaine_propre +=' '
    
print chaine_propre

