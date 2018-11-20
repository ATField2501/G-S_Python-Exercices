#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 49
# 5.8 Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des
# astérisques entre les caractères.
# Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »
	
import sys


neo_chaine=''

for arg in sys.argv: 
    chaine = arg

for e in chaine:
    neo_chaine += e+'*'

print "chaine de charactères initiale: {} qui devient : {}".format(chaine, neo_chaine)
