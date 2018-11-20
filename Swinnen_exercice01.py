#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 49
# 5.6 Écrivez un script qui détermine si une chaîne contient ou non le caractère « e ».
	
import sys

cible= 'e'

for arg in sys.argv: 
    chaine = arg


for e in chaine:
    if cible in e:
         boo=True
         break
    else:
         boo=False

if boo==True:
     print 'La chaine {} comporte au moins un {}'.format(arg, cible)
else:
     print 'La chaine {} ne comporte pas de {}'.format(arg, cible)
