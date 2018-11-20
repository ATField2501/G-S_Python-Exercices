#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>

# Exercice page 49

# 5.10. En partant de l'exercice précédent, écrivez un script qui détermine si une chaîne de
#caractères donnée est un palindrome (c'est-à-dire une chaîne qui peut se lire indifféremment
#dans les deux sens), comme par exemple « radar » ou « s.o.s ».


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

if arg == result:
    print "SUPER!! {} est un PALINDROME".format(arg)
else:
    print "Dommage.. Ce n'est pas un palindrome..."
