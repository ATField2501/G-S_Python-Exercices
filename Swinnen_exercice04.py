#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 49

# 5.9 Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l'inversant.
# Ainsi par exemple, « zorglub » deviendra « bulgroz ».

import sys

result=''

for arg in sys.argv: 
    chaine = arg
    chaine=list(chaine)
    neo = chaine
    neo.reverse()

for e in neo:
    result +=e


print "{} devient --> {}".format(arg, result)
